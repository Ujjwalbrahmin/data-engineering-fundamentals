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

# Cron expressions can be as simple as * * * * ? * or as complex as 0 0/5 14,18,3-39,52 ? JAN,MAR,SEP MON-FRI 2002-2010.
# in airflow CRON expression supports 5 placeholders(seconds omitted) same as AWS lambda
# https://crontab.guru/

with DAG(
        dag_id='cron-expression',
        default_args=defaults,
        start_date=datetime(2023, 3, 27),
        schedule_interval='0 12 * * *',
        catchup=True
) as dag:
    first_task = BashOperator(
        task_id='first_task',
        bash_command='python $AIRFLOW_HOME/codeSnippets/hello.py Brahmin'
    )
