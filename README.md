# Airflow workflow Example

For now, we will use virtual enviroments,
Based on https://www.youtube.com/watch?v=z7xyNOF8tak&t=4s and https://airflow.apache.org/docs/apache-airflow/stable/start/local.html
and https://github.com/apache/airflow/blob/master/airflow/providers/docker/example_dags/example_docker_copy_data.py
1) Create a virtual enviroment venv

Example
```
python3 -m venv venv
```

2) Activate the virtual enviroment.

3) Install apache-airflow

```
AIRFLOW_VERSION=2.0.1
PYTHON_VERSION="$(python --version | cut -d " " -f 2 | cut -d "." -f 1-2)"

CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"
pip install apache-airflow-providers-docker
```

4) Export airflow environment to the project directory

```
export AIRFLOW_HOME=.
```

5) initialize the database

```
airflow db init
```

6) Create an user

```
airflow users create \
    --username admin \
    --firstname Peter \
    --lastname Parker \
    --role Admin \
    --email spiderman@superhero.org
```

7) start the web server, default port is 8080
```
airflow webserver --port 8080
```

8) In a new terminal, start the scheduler

```
export AIRFLOW_HOME=.
airflow scheduler
```

9) In a new terminal, run dag script

```
export AIRFLOW_HOME=.
python dags/toy_example_dag.py 
```

10) set enable_xcom_pickling = True in airflow.cfg