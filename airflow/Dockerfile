FROM apache/airflow:2.3.0

USER root

COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

USER airflow

COPY dags /opt/airflow/dags

ENV AIRFLOW__CORE__EXECUTOR=LocalExecutor
ENV AIRFLOW__API__AUTH_BACKEND=airflow.api.auth.backend.basic

EXPOSE 8080