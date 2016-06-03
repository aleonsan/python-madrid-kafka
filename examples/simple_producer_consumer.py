#!/usr/bin/env python
import threading
import time

from kafka import KafkaConsumer, KafkaProducer

KAFKA_BROKERS = [
    'kafka1:9092',
    'kafka2:9092',
    'kafka3:9092',
]
KAFKA_PRODUCER_CONFIG = {
    'bootstrap_servers': KAFKA_BROKERS,
    'client_id': 'python_madrid_kafka01',
#    'key_serializer': None,
#    'value_serualizer': None,
#    'acks': 'all',
#    'compression_type': 'gzip',
#    'retries': '1',
#    'linger_ms': 0,
#    'partitioner': None,
#    'api_version': 'auto' 
}

KAFKA_CONSUMER_CONFIG = {
    'bootstrap_servers': KAFKA_BROKERS,
    'auto_offset_reset': 'earliest',
}


class Producer(threading.Thread):
#    daemon = True

    def run(self):
        producer = KafkaProducer(**KAFKA_PRODUCER_CONFIG)
        while True:
            producer.send('python-madrid', b"FOO")
            producer.send('python-madrid', b"BAR")
            producer.send('python-madrid', b"BAZ")
            time.sleep(5)


class Consumer(threading.Thread):
#    daemon = True

    def run(self):
        consumer = KafkaConsumer(**KAFKA_CONSUMER_CONFIG)
        consumer.subscribe(['ipython-madrid'])

        for message in consumer:
            print ("Something from the other side: ", message)


if __name__ == "__main__":

    threads = [
        Producer(),
        Consumer()
    ]

    for t in threads:
        t.start()

    time.sleep(10)
