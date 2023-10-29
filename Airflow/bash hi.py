from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.bash_operator import BashOperator

dag1 = DAG(
    dag_id='helloworld_dag1',  # Change the DAG ID to 'helloworld_dag1'
    schedule_interval="@daily",
    start_date=days_ago(1)
)

task1 = BashOperator(
    task_id='task1',
    bash_command='echo hello',
    dag=dag1  # Use dag1 here
)

task2 = BashOperator(
    task_id='task2',
    bash_command='echo t2',
    dag=dag1  # Use dag1 here
)

task3 = BashOperator(
    task_id='task3',
    bash_command='echo t3',
    dag=dag1  # Use dag1 here
)

task1 >> task2 >> task3
