#!/usr/bin/env python
import threading
import time

from kafka import KafkaConsumer

KAFKA_CONSUMER_CONFIG = {
    'bootstrap_servers': 'kafka1:9092',
#    'group_id': 'python_madrid',
}

if __name__ == "__main__":
        consumer = KafkaConsumer(**KAFKA_CONSUMER_CONFIG)
        consumer.subscribe(['python-madrid-demo'])
        print("These are my topics:", consumer.topics())
        for message in consumer:
            try:
                print (message.value)
            except KeyboardInterrupt:
                break 
