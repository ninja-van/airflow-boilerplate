# Airflow Boilerplate
A complete development environment setup for working with Airflow, based on the article (insert link here)

This boilerplate has more tools than was discussed in the article. In particular, it has the following things
that were not discussed in the article:
- A sample DAG
- A sample plugin
- A sample test for the plugin
- A sample helper method, `dags/common/stringcase.py`, accessible in both `dags/` and `plugins/`
- A sample test for the helper method
- A `spark-conf/` that is included in the Docker build step, you can explore this on your own
- A `.pre-commit-config.yaml`

# Getting Started

Install `docker` and `docker-compose` at:
- https://docs.docker.com/install/
- https://docs.docker.com/compose/install/

Clone this repo and `cd` into it:
```
git clone https://github.com/ninja-van/airflow-boilerplate.git && cd airflow-boilerplate
```

Create a virtualenv for this project. Feel free to choose your preferred way of managing Python virtual 
environments. I usually do it this way:
```
pip install virtualenv
virtualenv .venv
```

Activate the virtual environment:
```
source .venv/bin/activate
```

Install the requirements:
```
pip install -r requirements-airflow.txt
pip install -r requirements-dev.txt
```

Install the pre-commit hook:
```
pre-commit install
```
This will ensure for each commit, any file changes are gone through the linter and formatter. On top of that,
tests are ran, too, to make sure that nothing is broken.

# Setting up the Docker environment

Run the whole suit of Airflow components:
```
docker-compose -f docker/docker-compose.yml up -d
```
This brings up the Airflow `postgres` metadatabase, `scheduler`, and `webserver`.

To access the `webserver`, once the Docker container is up and healthy, go to `localhost:8080`. You can start
playing around with the samples DAGs. 

# Setting up PyCharm

Ensure that your Project Interpreter is pointing to the correct virtual environment.

![Ensure that your Project Interpreter is pointing to the correct virtual environment](/images/1_python_interpreter.png)

Mark both `dags/` and `plugins/` as source.

![Mark dags and plugins directories as "Sources Root"](/images/2_mark_as_source.png)

Run `source env.sh` on the terminal and copy the environment variables.

![Run env.sh and copy the env vars](/images/3_run_env_sh.png)

Add a new Run/Debug Configuration with the following parameters:  
- Name: `<whatever_you_want>`   
- Script path: `<path_to_your_virtualenv_airflow_binary>`
- Parameters: `test <dag_id> <task_id> <execution_date>` 
- Environment variables: `paste your env vars here`

![Run/debug configurations](/images/4_run_debug_config.png)

Add those environment variables to your test configuration (pytest in my case), so that you can just hit 
the run/debug button next to your test functions and they will work like a charm.

![Run/debug configurations](/images/5_pytest_template.png)

# Generating a new fernet key
Included in this boilerplate is a pre-generated fernet key. There should not be any security concern here
because after all you are meant to run this environment only locally. If you wish to have a new fernet key,
you can follow these steps below.

Generate a fernet key:
```
python -c "from cryptography.fernet import Fernet; FERNET_KEY = Fernet.generate_key().decode(); print(FERNET_KEY)"
```

Copy that fernet key to clipboard.
In `env.sh`, paste it here:
```
export AIRFLOW__CORE__FERNET_KEY=<YOUR_FERNET_KEY_HERE>
```

In `airflow.cfg`, paste it here:
```
fernet_key = <YOUR_FERNET_KEY_HERE>
```

# Concluding tips
- If you are only interested in just using your IDE, and you do not need the Airflow `scheduler` or `webserver`, run:
  ```
  docker-compose -f docker/docker-compose.yml up -d initdb
  ```

- To remove the examples from the Webserver, change the following line in the `airflow.cfg`:
  ```
  load_examples = False
  ```
  Notice that the `docker-compose` immediately picks up the changes in `airflow.cfg`.