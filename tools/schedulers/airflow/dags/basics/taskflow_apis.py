# libray imports
from datetime import datetime, timedelta
from airflow.decorators import task, dag

# custom imports

# defaults / globals
defaults = {
    'owner': 'ujjwal',
    'retries': 2,
    'retry_delay': timedelta(minutes=1)
}


@dag(dag_id='taskflow_apis',
     description='Using taskflow apis',
     default_args=defaults,
     start_date=datetime(2023, 3, 27),
     schedule_interval=timedelta(minutes=1)
     )
def hello_world():
    @task()
    def get_name(username):
        return username

    @task()
    def get_age():
        return 25

    @task()
    def greet_user(username, user_age):
        return f'Hello {username} {user_age} and welcome to the Airflow tutorials...'

    name = get_name('Ujjwal')
    age = get_age()

    greet_user(name, age)


greeting_dag = hello_world()
