"""
task.py
Defines the Task class and all database operations (CRUD).
Demonstrates OOP principles: encapsulation, methods, and data abstraction.
"""

from database import get_connection
from mysql.connector import Error

class Task:
    """Represents a single student task with all its attributes."""

    def __init__(self, title, subject, deadline, priority="Medium"):
        self.title = title
        self.subject = subject
        self.deadline = deadline   # expected format: YYYY-MM-DD
        self.priority = priority
        self.status = "Pending"

    def __str__(self):
        return (
            f"Title   : {self.title}\n"
            f"Subject : {self.subject}\n"
            f"Deadline: {self.deadline}\n"
            f"Priority: {self.priority}\n"
            f"Status  : {self.status}"
        )

    def save(self):
        """Insert this task into the database (CREATE)."""
        conn = get_connection()
        if conn is None:
            return False

        try:
            cursor = conn.cursor()
            query = """
                INSERT INTO tasks (title, subject, deadline, priority, status)
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(query, (
                self.title,
                self.subject,
                self.deadline,
                self.priority,
                self.status
            ))
            conn.commit()
            print(f"\n[✓] Task '{self.title}' added successfully!")
            return True
        except Error as e:
            print(f"[DB ERROR] Could not save task: {e}")
            return False
        finally:
            cursor.close()
            conn.close()

def get_all_tasks():
    """Fetch and return all tasks from the database (READ)."""
    conn = get_connection()
    if conn is None:
        return []

    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM tasks ORDER BY deadline ASC")
        return cursor.fetchall()
    except Error as e:
        print(f"[DB ERROR] Could not fetch tasks: {e}")
        return []
    finally:
        cursor.close()
        conn.close()

def mark_task_complete(task_id):
    """Mark a task as Completed by its ID (UPDATE)."""
    conn = get_connection()
    if conn is None:
        return

    try:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE tasks SET status = 'Completed' WHERE id = %s",
            (task_id,)
        )
        conn.commit()
        
        if cursor.rowcount == 0:
            print(f"[!] No task found with ID {task_id}.")
        else:
            print(f"[✓] Task {task_id} marked as Completed!")
    except Error as e:
        print(f"[DB ERROR] Could not update task: {e}")
    finally:
        cursor.close()
        conn.close()

def delete_task(task_id):
    """Delete a task by its ID (DELETE)."""
    conn = get_connection()
    if conn is None:
        return

    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
        conn.commit()
        
        if cursor.rowcount == 0:
            print(f"[!] No task found with ID {task_id}.")
        else:
            print(f"[✓] Task {task_id} deleted successfully!")
    except Error as e:
        print(f"[DB ERROR] Could not delete task: {e}")
    finally:
        cursor.close()
        conn.close()

def get_pending_tasks():
    """Return only tasks that are still Pending."""
    conn = get_connection()
    if conn is None:
        return []

    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute(
            "SELECT * FROM tasks WHERE status = 'Pending' ORDER BY deadline ASC"
        )
        return cursor.fetchall()
    except Error as e:
        print(f"[DB ERROR] {e}")
        return []
    finally:
        cursor.close()
        conn.close()