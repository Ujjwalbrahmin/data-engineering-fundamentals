# libray imports
from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator

# custom imports

# defaults / globals
defaults = {
    'owner': 'ujjwal',
    'retries': 2,
    'retry_delay': timedelta(minutes=1)
}

with DAG(
        dag_id='hello_upgrade_v2',
        description='This is hello world dag in airflow',
        default_args=defaults,
        start_date=datetime(2023, 1, 1),
        schedule=timedelta(minutes=1)
) as dag:
    first_task = BashOperator(
        task_id='task_1',
        email_on_failure=False,
        retries=2,
        retry_exponential_backoff=True,
        bash_command='echo Hello World !!!'
    )

    second_task = BashOperator(
        task_id='task_2',
        email_on_failure=False,
        retries=1,
        retry_exponential_backoff=False,
        do_xcom_push=False,
        bash_command='echo Hello India !!!'
    )

    third_task = BashOperator(
        task_id='task_3',
        email_on_failure=False,
        retries=1,
        retry_exponential_backoff=False,
        bash_command='echo Hello West bengal !!!'
    )

    first_task.set_downstream(second_task)
    first_task.set_downstream(third_task)

    # first_task >> second_task
    # first_task >> third_task

    # first_task >> [second_task, third_task]
