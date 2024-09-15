import time
import random

# Simulate health data collection from IoT devices
def collect_health_data():
    health_data = {
        'heart_rate': random.randint(60, 100),
        'activity_level': random.randint(1, 10),
        'temperature': random.uniform(98.0, 102.0)
    }
    return health_data

# Example usage
while True:
    data = collect_health_data()
    print(f"Collected Data: {data}")
    time.sleep(60)  # Wait for 60 seconds before collecting new data
