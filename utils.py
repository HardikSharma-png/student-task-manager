"""
utils.py
Utility functions: display helpers, input validators, date checker.
"""

from datetime import datetime

def print_banner(quote):
    width = 65
    print("\n" + "=" * width)
    print(" STUDENT TASK MANAGER ".center(width))
    print("=" * width)
    print(f"\n  {quote}\n")
    print("-" * width)

def print_menu():
    print("\n  MENU")
    print("  " + "-" * 29)
    print("  [1] Add New Task")
    print("  [2] View All Tasks")
    print("  [3] View Pending Tasks")
    print("  [4] Mark Task as Completed")
    print("  [5] Delete a Task")
    print("  [6] Export Tasks to CSV")
    print("  [0] Exit")
    print("  " + "-" * 29)

def display_tasks(tasks):
    if not tasks:
        print("\n  [!] No tasks to display.")
        return
        
    print(f"\n  {'ID':<5} {'TITLE':<25} {'SUBJECT':<15} {'DEADLINE':<12} {'PRIORITY':<10} {'STATUS'}")
    print("  " + "-" * 80)
    
    for t in tasks:
        print(f"  {t['id']:<5} {str(t['title']):<25} {str(t['subject']):<15} {str(t['deadline']):<12} {str(t['priority']):<10} {t['status']}")
    print()

def get_non_empty_input(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("  [!] This field cannot be empty.")

def get_valid_date(prompt):
    while True:
        date_str = input(prompt).strip()
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return date_str
        except ValueError:
            print("  [!] Use YYYY-MM-DD format (e.g. 2026-07-15).")

def get_valid_priority(prompt):
    valid = ["Low", "Medium", "High"]
    while True:
        choice = input(prompt).strip().capitalize()
        if choice in valid:
            return choice
        print(f"  [!] Enter one of: {', '.join(valid)}")

def get_valid_id(prompt):
    while True:
        try:
            value = int(input(prompt).strip())
            if value > 0:
                return value
            print("  [!] ID must be a positive number.")
        except ValueError:
            print("  [!] Please enter a valid numeric ID.")