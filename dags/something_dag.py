from datetime import timedelta

from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator

from airflow.operators.something_plugin import SomethingToSomethingOperator

from common.stringcase import snake_case

default_args = {
    "owner": "airflow",
    "start_date": "2020-05-13",
    "depends_on_past": False,
    "email": ["johndoe@abc.com"],
    "email_on_failure": True,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

dag_id = snake_case("SomethingDag")
with DAG(dag_id=dag_id, default_args=default_args, schedule_interval="@daily") as dag:
    main_task = SomethingToSomethingOperator(task_id="main_task")
    dummy_task = DummyOperator(task_id="dummy_task")
    main_task >> dummy_task
