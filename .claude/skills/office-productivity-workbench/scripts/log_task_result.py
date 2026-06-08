#!/usr/bin/env python3
"""Log a task result to logs/task_log.csv"""

import csv
import sys
import os
from datetime import datetime


def log_task(task, status, risk="low", notes=""):
    """Append a task record to logs/task_log.csv"""
    log_dir = os.path.join(os.getcwd(), "logs")
    os.makedirs(log_dir, exist_ok=True)

    log_file = os.path.join(log_dir, "task_log.csv")
    header = ["timestamp", "task", "status", "risk", "notes"]
    row = [
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        task,
        status,
        risk,
        notes,
    ]

    file_exists = os.path.isfile(log_file)
    with open(log_file, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(header)
        writer.writerow(row)

    print(f"[LOG] {row[0]} | {task} | {status}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: log_task_result.py <task> <status> [risk] [notes]")
        print("  task   - task description")
        print("  status - done / failed / skipped")
        print("  risk   - low / medium / high (default: low)")
        print("  notes  - optional notes")
        sys.exit(1)

    task = sys.argv[1]
    status = sys.argv[2]
    risk = sys.argv[3] if len(sys.argv) > 3 else "low"
    notes = sys.argv[4] if len(sys.argv) > 4 else ""
    log_task(task, status, risk, notes)
