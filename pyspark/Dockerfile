FROM apache/spark-py:latest

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY jobs /app/jobs

CMD ["spark-submit", "/app/jobs/etl_job.py"]