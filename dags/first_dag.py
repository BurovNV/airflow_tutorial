from airflow import DAG

from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

dag = DAG(
    "first_dag",
    start_date=days_ago(0, 0, 0, 0, 0),
    tags=['bash']
)

task_1 = BashOperator(
    bash_command="pwd",
    dag=dag,
    task_id='task_1'
)

task_2 = BashOperator(
    bash_command="sleep 5",
    dag=dag,
    task_id='task_2'
)

task_3 = BashOperator(
    bash_command="sleep 10",
    dag=dag,
    task_id='task_3'
)

task_4 = BashOperator(
    bash_command="echo 'completed' ",
    dag=dag,
    task_id='task_4'
)

# tasks

task_1 >> [task_2, task_3]

[task_2, task_3] >> task_4
