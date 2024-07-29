#!/usr/bin/python3
"""
This script fetches and displays the TODO list progress for a given employee ID
from a REST API and exports the data to a JSON file.

Requirements:
- Uses the requests module to make HTTP requests.
- Accepts an integer as a parameter, which is the employee ID.
- Displays the employee TODO list progress in the following format:
    First line: Employee EMPLOYEE_NAME is done with
    tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
        EMPLOYEE_NAME: name of the employee
        NUMBER_OF_DONE_TASKS: number of completed tasks
        TOTAL_NUMBER_OF_TASKS: total number of tasks,
        which is the sum of completed and non-completed tasks
    Second and N next lines display the title of completed tasks:
    TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE)
- Exports the TODO list data to a JSON file in the format:
    { "USER_ID": [{"task": "TASK_TITLE", "completed":
    TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}
  The file name must be: USER_ID.json

Example usage:
    python3 2-export_to_JSON.py 2
"""

import requests
import sys
import json


def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch employee data
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    if user_response.status_code != 200:
        print(f"User with ID {employee_id} not found.")
        return

    user_data = user_response.json()
    employee_name = user_data.get("username")

    # Fetch TODO list data
    todos_response = requests.get(f"{base_url}/todos?userId={employee_id}")
    if todos_response.status_code != 200:
        print(f"Could not fetch TODO list for user ID {employee_id}.")
        return

    todos_data = todos_response.json()

    # Prepare data for JSON export
    tasks = []
    for task in todos_data:
        tasks.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": employee_name
        })

    data = {str(employee_id): tasks}

    # Export to JSON
    json_filename = f"{employee_id}.json"
    with open(json_filename, mode='w') as file:
        json.dump(data, file)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    get_employee_todo_progress(employee_id)
