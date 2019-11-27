from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'Airflow',
    'depends_on_past': False,
    'start_date': datetime(2019, 11, 25),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG('password', default_args=default_args, schedule_interval=timedelta(days=1))


def import_csv_files():
    import pandas as pd
    import os
    import hashlib
    
    dirpath = os.path.realpath(__file__)
    dirpath = dirpath[:-15] # hard coded removing filename: "password_dag.py"
    # importing both given files into pandas dataframes
    clients = pd.read_csv('{0}/diac/ch4/clients.csv'.format(dirpath))
    possible_uuids = pd.read_csv('{0}/diac/ch4/possible_uuids.txt'.format(dirpath), 
        header=None, 
        names=["poss_uuid"])


t1 = PythonOperator(
    task_id='import_CSVs',
    python_callable=import_csv_files,
    ops_args=[], # a list of positional args that will get unpacked in py callable
    dag=dag)
t1
