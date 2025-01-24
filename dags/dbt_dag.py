from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='dbt_workflow',
    default_args=default_args,
    description='Run dbt models and generate docs',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2023, 1, 1),
    catchup=False,
) as dag:

    dbt_run = BashOperator(
        task_id='dbt_run',
        bash_command='docker exec -it dbt dbt run',
    )

    dbt_docs = BashOperator(
        task_id='dbt_docs',
        bash_command='docker exec -it dbt dbt docs generate',
    )

    dbt_run >> dbt_docs
