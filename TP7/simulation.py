import random
import time
from kafka import KafkaProducer
import json

# Connect to Kafka
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

topic = 'iot-sensor-data'

# Simulate sending data every few seconds
try:
    while True:
        sensor_data = {
            "temperature": round(random.uniform(20.0, 30.0), 2),
            "humidity": round(random.uniform(40.0, 70.0), 2),
            "pressure": round(random.uniform(1000.0, 1020.0), 2),
            "timestamp": time.strftime('%Y-%m-%d %H:%M:%S')
        }
        print(f"Sending: {sensor_data}")
        producer.send(topic, sensor_data)
        producer.flush()

        time.sleep(2)  # Wait 2 seconds between readings
except KeyboardInterrupt:
    print("Simulation stopped.")
