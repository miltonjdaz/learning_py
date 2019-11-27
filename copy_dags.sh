# kill and fill airflow_dags folder since symbolic link didn't work
rm -rf /home/milton/github/learning_py/airflow_dags
cp -rf /home/milton/airflow/dags /home/milton/github/learning_py/airflow_dags
