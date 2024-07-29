#!/usr/bin/python3
"""
This script fetches and records all tasks from all employees from a REST API
and exports the data to a JSON file.

Requirements:
- Uses the requests module to make HTTP requests.
- Records all tasks from all employees in the format:
    { "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE",
    "completed": TASK_COMPLETED_STATUS}, ... ]}
- The file name must be: todo_all_employees.json

Example usage:
    python3 3-dictionary_of_list_of_dictionaries.py
"""

import json
import requests


def fetch_all_employee_tasks():
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch all users
    users_response = requests.get(f"{base_url}/users")
    users = users_response.json()

    # Fetch all tasks
    todos_response = requests.get(f"{base_url}/todos")
    todos = todos_response.json()

    # Prepare data for JSON export
    data = {}
    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        user_tasks = [task for task in todos if task.get("userId") == user_id]
        data[user_id] = [
            {
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            for task in user_tasks
        ]

    # Export to JSON
    with open("todo_all_employees.json", "w") as file:
        json.dump(data, file)


if __name__ == "__main__":
    fetch_all_employee_tasks()
