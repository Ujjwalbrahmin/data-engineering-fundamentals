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

# catchup=True will catchup the time elapsed till start_date till utc.now() and will run based on scheduled interval
# we can do the similar thing using backfill command (scripts)
with DAG(
        dag_id='catch-up_and_back-fill_v2',
        default_args=defaults,
        start_date=datetime(2023, 3, 27),
        schedule_interval='@daily',
        catchup=False

) as dag:
    first_task = BashOperator(
        task_id='first_task',
        bash_command='python $AIRFLOW_HOME/codeSnippets/hello.py Ujjwal'
    )
