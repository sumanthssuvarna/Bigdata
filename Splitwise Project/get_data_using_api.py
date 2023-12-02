!pip install splitwise


from splitwise import Splitwise
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter, WeekdayLocator,\
    DayLocator, MONDAY
import datetime
from datetime import date, datetime, timedelta
import pandas as pd



class ExpenseTracker:
    
    def __init__(self, CONSUMER_KEY, CONSUMER_SECRET, API_KEY):
        self.sw = Splitwise(CONSUMER_KEY, CONSUMER_SECRET, api_key=API_KEY)
        self.expenses = []
    
    def get_expenses(self, target_days=365):
        current_page_num = 0
        page_size = 100
        end_date = date.today()
        start_date = end_date - timedelta(days=target_days)
        
        while True:
            curr_page_expenses = self.sw.getExpenses(
            dated_after=start_date,
            dated_before=end_date,
            limit=page_size,
            offset=current_page_num * page_size,
            )
            if len(curr_page_expenses) == 0:
                break
            current_page_num = current_page_num + 1
            self.expenses = self.expenses + curr_page_expenses
        return self.expenses


    def process_expense(self):
        # get current user ID
        my_user_id = self.sw.getCurrentUser().getId()
        
        my_expenses = []
        for expense in self.expenses:
            for user in expense.users:
                if user.id == my_user_id and expense.deleted_at is None and expense.description != "Payment":
                    my_expenses.append(expense)
            
        data = {'id': [], 'group':[], 'description': [], 'amount': [], 'my_cost':[], 'person':[],\
                            'currency': [], 'date': [], 'category': []}
        
        
        for expense in my_expenses:
            try:
                print(f"Before getGroup - expense ID: {expense.id}, Group ID: {expense.group_id}")
                group_name = self.sw.getGroup(expense.group_id).name if expense.group_id is not None else "0"
                print(f"After getGroup - Group Name: {group_name}")
                
                data['id'].append(str(expense.id) if expense.id is not None else "0")
                data['group'].append(group_name)
                data['description'].append(expense.description if expense.description is not None else "0")
                data['amount'].append(str(expense.cost) if expense.cost is not None else "0")
                my_cost = next((user.getNetBalance() for user in expense.getUsers() if user.id == my_user_id), 0)
                data['my_cost'].append(str(my_cost) if my_cost is not None else "0")
                person_name = next((user.getFirstName()+" "+user.getLastName() for user in expense.getUsers() if user.id != my_user_id), "0")
                data['person'].append(person_name)
                data['currency'].append(expense.currency_code if expense.currency_code is not None else "0")
                data['date'].append(str(expense.date) if expense.date is not None else "0")
                data['category'].append(expense.category.name if expense.category is not None else "0")
            except Exception as e:
                print(f"Error processing expense ID: {expense.id}, Group ID: {expense.group_id}")
                print(e)

        # Create DataFrame
        self.df = pd.DataFrame(data)

        return self.df
    
    
    # fix data types since by default all are in string formats
    def fix_datatypes(self):
        self.df['my_cost'] = pd.to_numeric(self.df['my_cost'])
        self.df['my_cost'] = self.df['my_cost'].abs()
        self.df.date = pd.to_datetime(self.df.date)
        self.df.amount = pd.to_numeric(self.df.amount)
        
    
    # return all group names in a list
    def get_group_names(self):
        return self.df["group"].to_list()
    
    
    # filter expense data based on particular group
    def get_group_expense(self, group_name):
        group_df = self.df.loc[self.df["group"] == group_name]
        return group_df
    
    
    
    
    
    #################################### VISUALIZATION #####################################
    
    def plot_monthly_group_expense(self, group_name):
        group_df = self.get_group_expense(group_name)
        group_df['amount'].groupby(group_df['date'].dt.to_period('M')).sum().plot(kind='bar')
    
        plt.xlabel('Month')
        plt.ylabel('Amount in USD')
        plt.title('Total group Expense per month')
        plt.show()
        
    
    def plot_all_categorical_expense(self):
        category_grp = self.df.groupby(self.df['category'])
        category_grp.amount.sum().plot(kind='bar')
        
        plt.ylabel('Amount in USD')
        plt.title('Expense by Category')
        plt.show()
        
        
    def plot_group_categorical_expense(self, group_name):
        group_df = self.get_group_expense(group_name)
        category_grp = group_df.groupby(group_df['category'])
        category_grp.amount.sum().plot(kind='bar')
        
        plt.ylabel('Amount in USD')
        plt.title('Expense by Category')
        plt.show()
        
        
    def plot_monthly_personal_expense(self):
        self.df['my_cost'].groupby(self.df['date'].dt.to_period('M')).sum().plot(kind='bar')
    
        plt.xlabel('Month')
        plt.ylabel('Amount in USD')
        plt.title('Total personal Expense per month')
        plt.show()
        
    
    def plot_monthly_personal_group_expense(self, group_name):
        group_df = self.get_group_expense(group_name)
        group_df['my_cost'].groupby(group_df['date'].dt.to_period('M')).sum().plot(kind='bar')
    
        plt.xlabel('Month')
        plt.ylabel('Amount in USD')
        plt.title('Total personal group Expense per month')
        plt.show()
        
        
    def plot_weekly_personal_expense(self):
        # # https://matplotlib.org/1.5.3/examples/pylab_examples/finance_demo.html
        mondays = WeekdayLocator(MONDAY)        # major ticks on the mondays
        alldays = DayLocator()              # minor ticks on the days
        weekFormatter = DateFormatter('%b %d')  # e.g., Jan 12
        dayFormatter = DateFormatter('%d')      # e.g., 12

        ax = plt.subplot(111)
        ax.bar(self.df.date, self.df.my_cost)
        ax.xaxis.set_major_locator(mondays)
        ax.xaxis.set_minor_locator(alldays)
        ax.xaxis.set_major_formatter(weekFormatter)
        plt.show()






# ... (previous code)

if __name__ == '__main__':
    CONSUMER_KEY = '0PXjvF9v9oIVHRIZ0YzbFxyV6l9whGvjMMYbWmm5'
    CONSUMER_SECRET = '44JfJfKu002kHKdNms4aF6APC8t65heKUwPVAKpD'
    API_KEY = 'fcenW7xrcSqtythpGGoAQMiT9K3PUBQjIxnLS1T2'
    
    my_sw = ExpenseTracker(CONSUMER_KEY, CONSUMER_SECRET, API_KEY)
    # change the number of days for your convenience
    my_sw.get_expenses(target_days=365)
    
    # Process the expenses and print the resulting DataFrame
    my_sw.process_expense()
    print(my_sw.df)

    # Example: Plot monthly group expense for a specific group
    my_sw.plot_monthly_group_expense("YourGroupName")

    # Add more calls to other visualization methods as needed
