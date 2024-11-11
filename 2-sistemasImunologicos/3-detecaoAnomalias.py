import numpy as np


def detect_anomalies(data, threshold=2):
    mean = np.mean(data)
    std_dev = np.std(data)
    anomalies = [value for value in data if abs(value - mean) > threshold * std_dev]
    return anomalies


data = [10, 12, 10, 11, 14, 100, 12, 11, 10, 13]
anomalies = detect_anomalies(data)
print(f"Anomalias detectadas: {anomalies}")
