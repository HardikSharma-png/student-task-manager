"""
main.py
Entry point for the Student Task Manager application.
Run this file to start the program: python main.py

Project  : Student Task Manager
Author   : Hardik Sharma
College  : Arya College of Engineering and IT, Jaipur
Branch   : Information Technology (5th Semester)
"""

import sys
from database import initialize_db
from task import Task, get_all_tasks, get_pending_tasks, mark_task_complete, delete_task
from api_helper import fetch_motivational_quote
from export import export_to_csv
from utils import (
    print_banner, print_menu, display_tasks,
    get_non_empty_input, get_valid_date,
    get_valid_priority, get_valid_id
)

def add_task():
    print("\n--- Add New Task ---")
    title = get_non_empty_input("Task Title: ")
    subject = get_non_empty_input("Subject: ")
    deadline = get_valid_date("Deadline (YYYY-MM-DD): ")
    priority = get_valid_priority("Priority (Low / Medium / High): ")

    new_task = Task(title, subject, deadline, priority)
    new_task.save()

def view_all():
    print("\n--- All Tasks ---")
    tasks = get_all_tasks()
    display_tasks(tasks)

def view_pending():
    print("\n--- Pending Tasks ---")
    tasks = get_pending_tasks()
    display_tasks(tasks)

def complete_task():
    print("\n--- Mark Task as Completed ---")
    view_all()
    task_id = get_valid_id("Enter Task ID to mark complete: ")
    mark_task_complete(task_id)

def remove_task():
    print("\n--- Delete a Task ---")
    view_all()
    task_id = get_valid_id("Enter Task ID to delete: ")
    confirm = input(f"Are you sure you want to delete Task {task_id}? (yes/no): ").strip().lower()
    
    if confirm == "yes":
        delete_task(task_id)
    else:
        print("[!] Delete cancelled.")

def export_tasks():
    print("\n--- Export Tasks to CSV ---")
    export_to_csv()

def main():
    # setup database table if missing
    initialize_db()

    # get quote and show banner
    print("\nFetching today's quote...")
    quote = fetch_motivational_quote()
    print_banner(quote)

    # main app loop
    while True:
        print_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            view_all()
        elif choice == "3":
            view_pending()
        elif choice == "4":
            complete_task()
        elif choice == "5":
            remove_task()
        elif choice == "6":
            export_tasks()
        elif choice == "0":
            print("\nGoodbye! Keep studying hard.\n")
            sys.exit(0)
        else:
            print("\n[!] Invalid choice. Please enter a number from the menu.")

if __name__ == "__main__":
    main()