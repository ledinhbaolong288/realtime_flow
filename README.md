# realtime_flow

## Overview
The `realtime_flow` project is a data pipeline that integrates various technologies to facilitate the extraction, transformation, and loading (ETL) of data from Amazon S3 to AWS Redshift, while also enabling real-time processing using Kafka. This project is built using Docker to ensure a consistent development and deployment environment.

## Architecture
The architecture of the project consists of the following components:

- **Data Source**: A CSV file located in an S3 bucket, containing 100 columns and approximately 1TB of data.
- **ETL Process**: Managed by Apache Airflow, which orchestrates the workflow of extracting data from S3, transforming it using PySpark, and loading it into AWS Redshift.
- **Real-Time Processing**: Implemented using Kafka, which allows for the streaming of data as it is ingested from S3.
- **Database**: AWS Redshift is used as the data warehouse for storing the transformed data.

## Project Structure
The project is organized into several directories, each serving a specific purpose:

- **airflow**: Contains the Airflow DAG definition, Dockerfile, and requirements for the Airflow service.
- **docker-compose.yml**: Defines the services, networks, and volumes for the entire application.
- **kafka**: Contains the Dockerfile and configuration for the Kafka service.
- **pyspark**: Contains the PySpark job for the ETL process, along with its Dockerfile and requirements.
- **redshift**: Contains the SQL schema definitions for the Redshift database.
- **s3**: Contains a sample CSV file that simulates the data source.
- **src**: Contains configuration settings, utility functions for ETL, and implementations for Kafka producer and consumer.
- **.env.example**: Provides an example of environment variables needed for the application.

## Setup Instructions
1. **Clone the Repository**: Clone this repository to your local machine.
2. **Docker Setup**: Ensure Docker and Docker Compose are installed on your machine.
3. **Environment Variables**: Copy `.env.example` to `.env` and fill in the necessary environment variables.
4. **Build and Run**: Use Docker Compose to build and run the services:
   ```
   docker-compose up --build
   ```
5. **Access Airflow**: Once the services are running, access the Airflow web interface to monitor and manage the ETL pipeline.

## Usage
- The ETL pipeline can be triggered manually or scheduled using Airflow.
- Kafka can be used to stream data in real-time as it is processed.
- Monitor the logs and outputs in the respective service containers for debugging and validation.

## Contributing
Contributions to the project are welcome. Please submit a pull request or open an issue for any enhancements or bug fixes.