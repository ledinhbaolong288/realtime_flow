# Configuration settings for the realtime_flow application

import os

class Config:
    # AWS S3 settings
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    S3_BUCKET_NAME = os.getenv('S3_BUCKET_NAME')
    S3_DATA_FILE = os.getenv('S3_DATA_FILE', 'sample_data.csv')

    # Redshift settings
    REDSHIFT_HOST = os.getenv('REDSHIFT_HOST')
    REDSHIFT_PORT = os.getenv('REDSHIFT_PORT', '5439')
    REDSHIFT_DB_NAME = os.getenv('REDSHIFT_DB_NAME')
    REDSHIFT_USER = os.getenv('REDSHIFT_USER')
    REDSHIFT_PASSWORD = os.getenv('REDSHIFT_PASSWORD')

    # Kafka settings
    KAFKA_BROKER_URL = os.getenv('KAFKA_BROKER_URL')
    KAFKA_TOPIC = os.getenv('KAFKA_TOPIC', 'data_topic')

    # General settings
    ETL_LOG_LEVEL = os.getenv('ETL_LOG_LEVEL', 'INFO')