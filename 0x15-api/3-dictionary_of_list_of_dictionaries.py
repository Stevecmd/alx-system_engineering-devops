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

import requests
import json


def fetch_all_employee_tasks():
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch all users
    users_response = requests.get(f"{base_url}/users")
    if users_response.status_code != 200:
        print("Could not fetch users.")
        return

    users_data = users_response.json()

    # Fetch all TODO tasks
    todos_response = requests.get(f"{base_url}/todos")
    if todos_response.status_code != 200:
        print("Could not fetch TODO tasks.")
        return

    todos_data = todos_response.json()

    # Organize data in the required format
    all_tasks = {}
    for user in users_data:
        user_id = user.get("id")
        username = user.get("username")
        user_tasks = [
            {
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            for task in todos_data if task.get("userId") == user_id
        ]
        all_tasks[str(user_id)] = user_tasks

    # Export to JSON
    json_filename = "todo_all_employees.json"
    with open(json_filename, mode='w') as file:
        json.dump(all_tasks, file)


if __name__ == "__main__":
    fetch_all_employee_tasks()
