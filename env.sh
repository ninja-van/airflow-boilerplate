# Set these env vars so that:
# 1. airflow commands locally are run against the docker postgres
# 2. `airflow test` runs properly

AIRFLOW_HOME=$(pwd)

# Note: env vars set here should be printed out in the print statement below
export AIRFLOW_HOME
export AIRFLOW__CORE__EXECUTOR=SequentialExecutor
export AIRFLOW__CORE__SQL_ALCHEMY_CONN=postgresql+psycopg2://airflow:airflow@localhost:5432/airflow
export AIRFLOW__CORE__FERNET_KEY="<YOUR_FERNET_KEY_HERE>"
export AIRFLOW__CORE__DAGS_FOLDER=$AIRFLOW_HOME/dags
export AIRFLOW__CORE__PLUGINS_FOLDER=$AIRFLOW_HOME/plugins
export AIRFLOW__CORE__BASE_LOG_FOLDER=$AIRFLOW_HOME/logs
export AIRFLOW__CORE__DAG_PROCESSOR_MANAGER_LOG_LOCATION=$AIRFLOW_HOME/logs/dag_processor_manager/dag_processor_manager.log
export AIRFLOW__SCHEDULER__CHILD_PROCESS_LOG_DIRECTORY=$AIRFLOW_HOME/logs/scheduler

print \
"===================================================================
Environment Variables for Local Execution (vs execution in Docker)
===================================================================
AIRFLOW_HOME=$AIRFLOW_HOME
AIRFLOW__CORE__EXECUTOR=$AIRFLOW__CORE__EXECUTOR
AIRFLOW__CORE__SQL_ALCHEMY_CONN=$AIRFLOW__CORE__SQL_ALCHEMY_CONN
AIRFLOW__CORE__FERNET_KEY=$AIRFLOW__CORE__FERNET_KEY
AIRFLOW__CORE__DAGS_FOLDER=$AIRFLOW__CORE__DAGS_FOLDER
AIRFLOW__CORE__PLUGINS_FOLDER=$AIRFLOW__CORE__PLUGINS_FOLDER
AIRFLOW__CORE__BASE_LOG_FOLDER=$AIRFLOW__CORE__BASE_LOG_FOLDER
AIRFLOW__CORE__DAG_PROCESSOR_MANAGER_LOG_LOCATION=$AIRFLOW__CORE__DAG_PROCESSOR_MANAGER_LOG_LOCATION
AIRFLOW__SCHEDULER__CHILD_PROCESS_LOG_DIRECTORY=$AIRFLOW__SCHEDULER__CHILD_PROCESS_LOG_DIRECTORY
"
