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

import json
import requests
import sys


# Define base URL
BASE_URL = "https://jsonplaceholder.typicode.com/"


def get_user_data(user_id):
    """
    Fetch user data and TODO list for the given user ID.
    """
    user_response = requests.get(f"{BASE_URL}users/{user_id}")
    if user_response.status_code != 200:
        print(f"User with ID {user_id} not found.")
        sys.exit(1)

    user = user_response.json()
    username = user.get("username")

    todos_response = requests.get(
        f"{BASE_URL}todos",
        params={"userId": user_id}
    )
    if todos_response.status_code != 200:
        print(f"Could not fetch TODO list for user ID {user_id}.")
        sys.exit(1)

    todos = todos_response.json()
    return user_id, username, todos


def export_to_json(filename, data):
    """
    Export data to a JSON file with the specified filename.
    """
    tasks = [
        {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": data[1]
        } for task in data[2]
    ]
    data_to_export = {str(data[0]): tasks}

    with open(f"{filename}.json", "w") as jsonfile:
        json.dump(data_to_export, jsonfile, indent=4)


def main():
    """
    Main function to handle user input and process the TODO list.
    """
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    user_data = get_user_data(employee_id)
    export_to_json(employee_id, user_data)
    print(
        f"Data for employee ID {employee_id} has been exported to "
        f"{employee_id}.json"
    )


if __name__ == "__main__":
    main()
