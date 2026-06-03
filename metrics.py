def format_metrics(node_id, cpu, memory, processes):
    return {
        "node_id": node_id,
        "cpu": cpu,
        "memory": memory,
        "process_count": processes
    }
