from pyspark.sql import SparkSession
from pyspark.sql import DataFrame
import boto3
import os

def create_spark_session() -> SparkSession:
    spark = SparkSession.builder \
        .appName("ETL Job") \
        .getOrCreate()
    return spark

def read_data_from_s3(spark: SparkSession, s3_path: str) -> DataFrame:
    df = spark.read.csv(s3_path, header=True, inferSchema=True)
    return df

def transform_data(df: DataFrame) -> DataFrame:
    # Example transformation: Select specific columns and filter rows
    transformed_df = df.select("column1", "column2", "column3") \
                       .filter(df["column1"].isNotNull())
    return transformed_df

def write_data_to_redshift(df: DataFrame, redshift_table: str, redshift_url: str, user: str, password: str):
    df.write \
        .format("com.databricks.spark.redshift") \
        .option("url", redshift_url) \
        .option("dbtable", redshift_table) \
        .option("user", user) \
        .option("password", password) \
        .mode("overwrite") \
        .save()

def main():
    spark = create_spark_session()
    
    s3_bucket = os.getenv("S3_BUCKET")
    s3_file = os.getenv("S3_FILE")
    s3_path = f"s3a://{s3_bucket}/{s3_file}"
    
    redshift_table = os.getenv("REDSHIFT_TABLE")
    redshift_url = os.getenv("REDSHIFT_URL")
    user = os.getenv("REDSHIFT_USER")
    password = os.getenv("REDSHIFT_PASSWORD")
    
    df = read_data_from_s3(spark, s3_path)
    transformed_df = transform_data(df)
    write_data_to_redshift(transformed_df, redshift_table, redshift_url, user, password)
    
    spark.stop()

if __name__ == "__main__":
    main()