# SciCluster Monitor

A lightweight distributed systems monitoring platform simulating scientific cluster workloads using a node-agent architecture and centralized controller.

## 🚀 Overview

SciCluster Monitor is a Python-based distributed system that simulates a multi-node scientific computing environment. Each node runs an agent that collects system metrics and sends them to a central controller for aggregation, monitoring, and logging.

This project demonstrates core distributed systems concepts such as:
- Node-agent architecture
- Centralized coordination
- System observability
- Fault visibility and workload tracking

---

## 🧠 System Architecture

### 1. Node Agent
- Runs on each compute node
- Collects system metrics (CPU, memory, process count)
- Sends data to central controller via REST API

### 2. Central Controller
- Receives metrics from all nodes
- Maintains cluster state
- Logs system-wide activity
- Provides cluster status endpoint

---

## ⚙️ Tech Stack
- Python
- Flask (REST API)
- psutil (system monitoring)
- Requests (communication layer)
- Linux environment

---

## 📁 Project Structure

agent/ → Node-side metric collector  
controller/ → Central monitoring server  
shared/ → Common data structures  
logs/ → Cluster activity logs  

---

## 🚀 How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
