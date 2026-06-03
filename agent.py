import psutil
import requests
import time

CONTROLLER_URL = "http://127.0.0.1:5000/report"
NODE_ID = "node-1"

def collect_metrics():
    return {
        "node_id": NODE_ID,
        "cpu": psutil.cpu_percent(interval=1),
        "memory": psutil.virtual_memory().percent,
        "process_count": len(psutil.pids())
    }

while True:
    try:
        data = collect_metrics()
        requests.post(CONTROLLER_URL, json=data)
        print("Sent:", data)
    except Exception as e:
        print("Error:", e)

    time.sleep(5)
