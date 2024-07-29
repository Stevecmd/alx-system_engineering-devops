#!/usr/bin/python3

"""
Fetches and records all tasks from a specific employee
from a REST API and exports the data to a JSON file.
"""

import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <user_id>")
        sys.exit(1)

    user_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch user
    user_response = requests.get(
        base_url + "users/{}".format(employee_id)
    ).json()
    if user_response.status_code != 200:
        print("Could not fetch user.")
        sys.exit(1)

    user_data = user_response.json()
    username = user_data.get("username")
    name = user_data.get("name")

    # Fetch TODO tasks for the user
    todos_response = requests.get(
        f"{base_url}/todos",
        params={"userId": user_id}
    )
    if todos_response.status_code != 200:
        print("Could not fetch TODO tasks.")
        sys.exit(1)

    todos_data = todos_response.json()

    # Organize data in the required format
    completed_tasks = [task for task in todos_data if task.get("completed")]
    total_tasks = len(todos_data)
    completed_count = len(completed_tasks)

    # Print the tasks in the desired format
    print(
        f"Employee {name} is done with tasks("
        f"{completed_count}/{total_tasks}):"
    )
    for task in completed_tasks:
        print(f"\t {task.get('title')}")

    # Export to JSON
    all_tasks = {
        str(user_id): [
            {
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            for task in todos_data
        ]
    }

    json_filename = "todo_all_employees.json"
    with open(json_filename, mode='w') as file:
        json.dump(all_tasks, file)
