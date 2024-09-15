import threading
from data_collector import collect_health_data
from data_sender import send_data_to_server

def collect_and_send_data():
    """
    Collects data and sends it to the server in a separate thread.
    """
    while True:
        data = collect_health_data()
        send_data_to_server(data)
        time.sleep(60)  # Collect and send data every 60 seconds

def main():
    """
    Main function to start the IoT system.
    """
    # Run the data collection and sending in a separate thread
    data_thread = threading.Thread(target=collect_and_send_data)
    data_thread.start()

if __name__ == "__main__":
    main()
