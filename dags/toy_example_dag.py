from datetime import timedelta

from airflow import DAG

from airflow.providers.docker.operators.docker import DockerOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'ml-example-docker',
    default_args=default_args,
    description='A simple ml example',
    schedule_interval=timedelta(days=1),
    start_date=days_ago(2),
    tags=['example'],
)

t1 = DockerOperator(
    task_id='preprocessing-step',
    image='warvito/preprocessing-airflow:v1',
    command="python run.py",
    dag=dag,
)

t2 = DockerOperator(
    task_id='classification-step',
    image='warvito/toy-example-classifier-airflow:v1',
    command="python run.py",
    dag=dag,
)

t1 >> t2