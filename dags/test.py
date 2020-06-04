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

dag = DAG('test2',
          default_args=default_args,
          description='AnhTV test',
          schedule_interval='@once',
          start_date=datetime(2018, 1, 1, tzinfo=pendulum.timezone('Asia/Ho_Chi_Minh')),
          catchup=False)

t1 = BashOperator(
    task_id="test2",
    bash_command="/home/vuviethung/code/cenjobs/test/run-test.sh",
    dag=dag,
)
