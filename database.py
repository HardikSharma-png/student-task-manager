"""
database.py
Handles MySQL connection and table creation for Student Task Manager.
"""

import mysql.connector
from mysql.connector import Error

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "h1ard6ik8s",
    "database": "taskdb"
}

def get_connection():
    """Create and return a MySQL connection."""
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except Error as e:
        print(f"[DB ERROR] Could not connect to MySQL: {e}")
        return None

def initialize_db():
    """Create the tasks table if it doesn't already exist."""
    conn = get_connection()
    if conn is None:
        return

    try:
        cursor = conn.cursor()

        # Create database if not exists (safety net)
        cursor.execute("CREATE DATABASE IF NOT EXISTS taskdb")
        cursor.execute("USE taskdb")

        create_table_query = """
        CREATE TABLE IF NOT EXISTS tasks (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            subject VARCHAR(100) NOT NULL,
            deadline DATE NOT NULL,
            priority ENUM('Low', 'Medium', 'High') DEFAULT 'Medium',
            status ENUM('Pending', 'Completed') DEFAULT 'Pending',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
        cursor.execute(create_table_query)
        conn.commit()
        print("[DB] Database initialized successfully.")
        
    except Error as e:
        print(f"[DB ERROR] Table creation failed: {e}")
        
    finally:
        # cleanup
        cursor.close()
        conn.close()