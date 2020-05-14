import os
import pytest

from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.models import DagBag

DAGS_FOLDER = os.environ["AIRFLOW__CORE__DAGS_FOLDER"]


@pytest.fixture(scope="session")
def dag_bag():
    return DagBag(dag_folder=DAGS_FOLDER, include_examples=False)


@pytest.fixture
def dag():
    default_args = {"owner": "airflow", "start_date": days_ago(1)}
    return DAG("test_dag", default_args=default_args, schedule_interval="@daily")
