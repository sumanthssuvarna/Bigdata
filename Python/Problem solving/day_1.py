#o/p: [12, 8, 6, 4, 2]
#Only even in descending order
input_list = [2,6,12, 5, 8, 21, 4, 17, 9]
even=[i for i in input_list if i%2==0]
even.sort(reverse=True)
print(even)


#You are given a list of tuples, each representing a person's name and age.
#  Create a function that takes this list as input and returns a dictionary where the names are keys, 
#  and the values are lists of ages for each person with that name.
input_list = [("Alice", 25), ("Bob", 30), ("Alice", 28), ("Charlie", 25)]
a={}
for b,c in input_list:
  if b in a:
    a[b].append(c)
  else:
    a[b]=[c]
a
#output
# {
#     'Alice': [25, 28],
#     'Bob': [30],
#     'Charlie': [25]
# }



# Problem 3: Set Operations
# Write a function that takes two sets as input and returns a set containing all the 
# elements that are common to both sets, 
# as well as the elements that are unique to each set. 
# This set should be sorted in ascending order.

b = {2, 4, 6, 8, 10}
c = {5, 6, 7, 8, 9}

a=b.union(c)-b.intersection(c)
a

#o/p: {2, 4, 5, 7, 9, 10}


shopping_cart = {'apple': 5, 'banana': 3, 'orange': 4, 'grapes': 2}
discount_items = ['apple', 'grapes']

for i,j in shopping_cart.items():
  if i in discount_items:
    shopping_cart[i]=shopping_cart[i]-1

shopping_cart

#{'apple': 4, 'banana': 3, 'orange': 4, 'grapes': 1}



student_data = [
    ('Alice', {'Math', 'Physics', 'Chemistry'}, [88, 92, 78]),
    ('Bob', {'Math', 'English'}, [76, 84]),
    ('Charlie', {'Physics', 'History'}, [90, 88]),
    ('David', {'Math', 'Chemistry'}, [82, 95])
]


a={}
for i,j,k in student_data:
  a[i]=(sum(k)/len(k))

a

# {
#     'Alice': 86.0,
#     'Bob': 80.0,
#     'Charlie': 89.0,
#     'David': 88.5
# }


# S = "practice"
# Output: prectica
# Explanation: The vowels are a, i, e
# Reverse of these is e, i, a.
S = "practice"
s=list(S)
ovel=[]
for i in s:
  if i in ['a','e','i','o','u']:
    ovel.append(i)
z=-1
for i in range(len(s)):
  if s[i] in ['a','e','i','o','u']:
    s[i]=ovel[z]
    z=z-1
print("".join(s))


# Output: prectica