from datetime import timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'armaanPy',
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    'hello_world_DAG',
    default_args=default_args,
    schedule_interval=None, # No automatic scheduling.
    catchup=False           # Do not catchup on missed intervals.
) as dag:
    # Define the Bash task.
    hello_world_task = BashOperator(
        task_id='hello_world_task',
        bash_command='echo "Hello World!'
    )
