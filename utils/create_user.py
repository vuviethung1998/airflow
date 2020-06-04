from airflow import models, settings
from airflow.contrib.auth.backends.password_auth import PasswordUser
user = PasswordUser(models.User())
user.username = 'hungvv1'
user.email = 'user@email.com'
user.password = 'hungvv'

# the secret sauce is right here
from sqlalchemy import create_engine

if __name__=="__main_":
    engine = create_engine("postgresql://airflow:airflow@postgres:5432/airflow")

    session = settings.Session(bind=engine)
    session.add(user)
    session.commit()
    session.close()
    exit()
