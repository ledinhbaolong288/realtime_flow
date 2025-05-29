from kafka import KafkaProducer
import pandas as pd
import json
import os

class KafkaDataProducer:
    def __init__(self, topic, bootstrap_servers):
        self.topic = topic
        self.producer = KafkaProducer(
            bootstrap_servers=bootstrap_servers,
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )

    def send_data(self, data):
        for record in data:
            self.producer.send(self.topic, record)
        self.producer.flush()

def read_csv_and_produce(file_path, topic, bootstrap_servers):
    producer = KafkaDataProducer(topic, bootstrap_servers)
    data = pd.read_csv(file_path)
    records = data.to_dict(orient='records')
    producer.send_data(records)

if __name__ == "__main__":
    file_path = os.getenv('CSV_FILE_PATH', 's3/sample_data.csv')
    topic = os.getenv('KAFKA_TOPIC', 'your_topic_name')
    bootstrap_servers = os.getenv('KAFKA_BOOTSTRAP_SERVERS', 'localhost:9092')
    
    read_csv_and_produce(file_path, topic, bootstrap_servers)