"""
export.py
Exports all tasks to a CSV file.
Demonstrates: csv module, file handling, datetime module.
"""

import csv
import os
from datetime import datetime
from task import get_all_tasks

def export_to_csv():
    """Fetch all tasks from DB and write them to a timestamped CSV file."""
    tasks = get_all_tasks()

    if not tasks:
        print("[!] No tasks found to export.")
        return

    # Create exports folder if it doesn't exist
    os.makedirs("exports", exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"exports/tasks_{timestamp}.csv"

    fieldnames = ["id", "title", "subject", "deadline", "priority", "status", "created_at"]

    try:
        with open(filename, mode="w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            
            for task in tasks:
                writer.writerow({field: task.get(field, "") for field in fieldnames})

        print(f"[✓] Tasks exported successfully to '{filename}'")

    except IOError as e:
        print(f"[FILE ERROR] Could not write CSV: {e}")