from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
import pendulum

default_args = {
    'owner': 'anhtv',
    'email': ['tranvietanh.hust@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': True
}

dag = DAG('test_',
          default_args=default_args,
          description='AnhTV test',
          schedule_interval='@once',
          start_date=datetime(2018, 1, 1, tzinfo=pendulum.timezone('Asia/Ho_Chi_Minh')),
          catchup=False)

t1 = BashOperator(
    task_id="watermark_for_dcs",
    bash_command="/home/vuviethung/code/code/cen_jobs/project_statistics_monthly/run-project-filtering.sh",
    dag=dag,
)
