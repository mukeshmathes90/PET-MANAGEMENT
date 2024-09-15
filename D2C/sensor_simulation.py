import random

def generate_sensor_data():
    """
    Simulates sensor data for pet health monitoring.
    Returns a dictionary with simulated metrics.
    """
    data = {
        'heart_rate': random.randint(60, 100),  # Heart rate in bpm
        'activity_level': random.randint(1, 10),  # Activity level on a scale from 1 to 10
        'temperature': random.uniform(98.0, 102.0)  # Temperature in Fahrenheit
    }
    return data
