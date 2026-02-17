import numpy as np


def detect_anomalies(values: list[float], threshold: float = 2.0) -> list[dict]:
    """Detect anomalies using z-score method."""
    if len(values) < 3:
        return []

    arr = np.array(values)
    mean = np.mean(arr)
    std = np.std(arr)

    if std == 0:
        return []

    anomalies = []
    for i, v in enumerate(values):
        z = abs((v - mean) / std)
        if z > threshold:
            anomalies.append({"index": i, "value": v, "z_score": round(float(z), 3)})

    return anomalies
