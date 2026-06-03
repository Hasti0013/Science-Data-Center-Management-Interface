import requests
import time

for i in range(5):
    r = requests.get("http://127.0.0.1:5000/cluster")
    print("Cluster State:", r.json())
    time.sleep(3)
