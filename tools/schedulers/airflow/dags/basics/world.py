# libray imports
from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator

# custom imports

# defaults / globals
defaults = {
    'owner': 'ujjwal',
    'retries': 2,
    'retry_delay': timedelta(minutes=1)
}


class Greetings:
    @staticmethod
    def get_name(name):
        return name

    @staticmethod
    def get_age(ti):
        default_name = ti.xcom_pull()
        print(f"Hello {default_name}, this is your default name which had been passed")
        ti.xcom_push(key='age', value=25)
        ti.xcom_push(key='name', value='Brahmin')

    @staticmethod
    def greetings_with_name(ti):
        name = ti.xcom_pull(task_ids='get_age', key='name')

        return f'Hello {name} and welcome to airflow tutorial...'

    @staticmethod
    def greetings_with_name_and_age(ti):
        name = ti.xcom_pull(task_ids='get_name')
        age = ti.xcom_pull(task_ids='get_age', key='age')
        default_message = ti.xcom_pull()

        print(f" Default message : {default_message}")
        return f'Hello {name} : {age} and welcome to airflow tutorial...'


with DAG(
        dag_id='world_upgraded_v4',
        description='Python operator dag',
        default_args=defaults,
        start_date=datetime(2023, 1, 1),
        schedule=timedelta(minutes=1)
) as dag:
    first_task = PythonOperator(
        task_id='get_name',
        python_callable=Greetings.get_name,
        op_kwargs={'name': 'Ujjwal'}
    )
    second_task = PythonOperator(
        task_id='get_age',
        python_callable=Greetings.get_age,
        op_kwargs={}
    )

    third_task = PythonOperator(
        task_id='greet_user_with_name',
        python_callable=Greetings.greetings_with_name
    )

    fourth_task = PythonOperator(
        task_id='greet_user_with_name_and_age',
        python_callable=Greetings.greetings_with_name_and_age
    )

    [first_task, second_task] >> fourth_task
    # first_task >> second_task >> third_task >> fourth_task
