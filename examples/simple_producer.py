#!/usr/bin/env python
import threading
import time

from kafka import KafkaProducer

KAFKA_PRODUCER_CONFIG = {
    'bootstrap_servers': 'kafka1:9092',
#    'client_id': 'python_madrid_kafka01',
}

messages = [b'*****   *     *  ******', b'*    *     *     *', b'*    *  *     *  *',
            b'*    *     *     *', b'*    *     *     ****', b'*    *   *   *   *',
            b'****      * *    *', b'*****      *     ******']
message_order = [0, 2, 2, 5, 6, 3, 4, 1, 1, 7]
if __name__ == "__main__":
    producer = KafkaProducer(**KAFKA_PRODUCER_CONFIG)

    for m in message_order:
        producer.send('python-madrid-demo', messages[m])
    
    producer.flush()
