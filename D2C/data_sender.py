import requests
from data_collector import collect_health_data

def send_data_to_server(data):
    """
    Sends collected data to a remote server.
    """
    server_url = "http://example.com/health_data"  # Replace with actual server URL
    try:
        response = requests.post(server_url, json=data)
        response.raise_for_status()  # Raise HTTPError for bad responses
        print(f"Data sent successfully: {data}")
    except requests.exceptions.RequestException as e:
        print(f"Error sending data: {e}")

def main():
    """
    Collects data and sends it to the server.
    """
    while True:
        data = collect_health_data()
        send_data_to_server(data)
        time.sleep(60)  # Send data every 60 seconds

if __name__ == "__main__":
    main()
