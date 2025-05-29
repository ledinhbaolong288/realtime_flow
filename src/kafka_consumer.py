from kafka import KafkaConsumer
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def consume_messages(topic, bootstrap_servers):
    consumer = KafkaConsumer(
        topic,
        bootstrap_servers=bootstrap_servers,
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='my-group',
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )

    try:
        for message in consumer:
            logger.info(f"Received message: {message.value}")
            # Process the message (e.g., trigger ETL job, store in database, etc.)
    except Exception as e:
        logger.error(f"Error while consuming messages: {e}")
    finally:
        consumer.close()

if __name__ == "__main__":
    consume_messages('your_topic_name', 'localhost:9092')