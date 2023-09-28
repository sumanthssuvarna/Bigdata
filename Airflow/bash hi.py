from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.bash_operator import BashOperator

dag = DAG(
    dag_id='helloworld_dag',
    schedule_interval="@daily",
    start_date=days_ago(1)
)

task1 = BashOperator(
    task_id='task1',
    bash_command='echo hello',
    dag=dag
)

task2 = BashOperator(
    task_id='task2',
    bash_command='echo t2',
    dag=dag
)

task3 = BashOperator(
    task_id='task3',
    bash_command='echo t3',
    dag=dag
)

task1 >> task2 >> task3
