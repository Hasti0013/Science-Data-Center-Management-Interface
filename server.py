from flask import Flask, request
import datetime

app = Flask(__name__)

cluster_state = {}

@app.route("/report", methods=["POST"])
def report():
    data = request.json
    node = data["node_id"]

    cluster_state[node] = data

    log_line = f"{datetime.datetime.now()} | {data}\n"
    print(log_line)

    return {"status": "received"}

@app.route("/cluster", methods=["GET"])
def cluster():
    return cluster_state

if __name__ == "__main__":
    app.run(port=5000)
