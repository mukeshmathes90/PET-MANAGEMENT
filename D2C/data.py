import requests
import random
import time

def collect_health_data():
    health_data = {
        'heart_rate': random.randint(60, 100),
        'activity_level': random.randint(1, 10),
        'temperature': random.uniform(98.0, 102.0)
    }
    return health_data

def send_data_to_server(data):
    server_url = "http://example.com/health_data"  
    try:
        response = requests.post(server_url, json=data)
        response.raise_for_status()  
        print(f"Data sent successfully: {data}")
    except requests.exceptions.RequestException as e:
        print(f"Error sending data: {e}")

def main():
    while True:
        data = collect_health_data()
        send_data_to_server(data)
        time.sleep(60)

if __name__ == "__main__":
    main()
