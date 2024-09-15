import time
from sensor_simulation import generate_sensor_data

def collect_health_data():
    """
    Collects health data from simulated sensors.
    """
    data = generate_sensor_data()
    return data

def main():
    """
    Continuously collects data and prints it.
    """
    while True:
        data = collect_health_data()
        print(f"Collected Data: {data}")
        time.sleep(60)  # Collect data every 60 seconds

if __name__ == "__main__":
    main()
