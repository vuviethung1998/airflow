from datetime import datetime

import pendulum
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {
    'owner': 'hungvv1',
    'email': ['vuviethung.98.hust@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': True
}

dag = DAG('project_analytics_monthly',
            default_args=default_args,
            description='Các jobs chạy phân tích dự án theo tháng',
            schedule_interval='@once',
            start_date=datetime(2018, 1, 1, tzinfo=pendulum.timezone('Asia/Ho_Chi_Minh')),
            catchup=False
        )

t1 = BashOperator(
    task_id="project_statistics_monthly",
    bash_command='/home/vuviethung/code/code/cen_jobs/project_statistics_monthly/run-project-filtering.sh',
    dag=dag,
)
