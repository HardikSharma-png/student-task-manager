# 🎓 Student Task Manager

A command-line application built in Python that helps students manage their academic tasks with deadline tracking, priority levels, and motivational quotes.

## Project Details

| Field      | Info                                      |
|------------|-------------------------------------------|
| Author     | Hardik Sharma                             |
| College    | Arya College of Engineering, Jaipur       |
| Branch     | Information Technology — 5th Semester     |
| Language   | Python 3.x                                |
| Database   | MySQL                                     |

---

## Features

- Add tasks with title, subject, deadline, and priority
- View all tasks or filter by pending status
- Mark tasks as completed
- Delete tasks
- Export all tasks to a timestamped CSV file
- Fetches a motivational quote from an API on startup
- Graceful error handling throughout

---

## Concepts Covered

| Concept                  | Where Used                        |
|--------------------------|-----------------------------------|
| Variables & Data Types   | All files                         |
| Functions & Modules      | utils.py, export.py, api_helper.py|
| OOP (Class & Methods)    | task.py — Task class              |
| Exception Handling       | database.py, api_helper.py        |
| File Handling            | export.py — CSV writing           |
| MySQL Database (CRUD)    | database.py, task.py              |
| API Integration          | api_helper.py — Quotable API      |
| CLI Input/Output         | main.py, utils.py                 |
| Loops & Conditionals     | main.py — menu loop               |

---

## Project Structure

```
student_task_manager/
│
├── main.py          # Entry point — CLI menu loop
├── task.py          # Task class + CRUD operations
├── database.py      # MySQL connection + table setup
├── api_helper.py    # Motivational quote API
├── export.py        # CSV export functionality
├── utils.py         # Display helpers + input validators
├── requirements.txt # Python dependencies
└── README.md        # Project documentation
```

---

## Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/student-task-manager.git
cd student-task-manager
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up MySQL
Open MySQL and run:
```sql
CREATE DATABASE taskdb;
```

### 4. Configure password
Open `database.py` and replace `h1ard6ik8s` with your actual MySQL root password.

### 5. Run the app
```bash
python main.py
```

---

## How It Works

1. On startup, the app connects to MySQL and creates the `tasks` table if it doesn't exist
2. It fetches a motivational quote from the [Quotable API](https://api.quotable.io)
3. The main menu loop lets you perform all task operations
4. All data is stored persistently in MySQL
5. You can export a snapshot of your tasks to CSV at any time

---

## Database Schema

```sql
CREATE TABLE tasks (
    id          INT AUTO_INCREMENT PRIMARY KEY,
    title       VARCHAR(255)    NOT NULL,
    subject     VARCHAR(100)    NOT NULL,
    deadline    DATE            NOT NULL,
    priority    ENUM('Low', 'Medium', 'High') DEFAULT 'Medium',
    status      ENUM('Pending', 'Completed')  DEFAULT 'Pending',
    created_at  TIMESTAMP       DEFAULT CURRENT_TIMESTAMP
);
```
