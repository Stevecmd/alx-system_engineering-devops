#!/usr/bin/python3
"""
This script fetches and displays the TODO list progress for a given employee ID
from a REST API.

Requirements:
- Uses the requests module to make HTTP requests.
- Accepts an integer as a parameter, which is the employee ID.
- Displays the employee TODO list progress in the following format:
    First line: Employee EMPLOYEE_NAME is done with tasks:
        EMPLOYEE_NAME: name of the employee
        NUMBER_OF_DONE_TASKS: number of completed tasks
        TOTAL_NUMBER_OF_TASKS: total number of tasks
Example usage:
    python3 0-gather_data_from_an_API.py 2

"""

import requests
import sys


def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch employee data
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    if user_response.status_code != 200:
        print(f"User with ID {employee_id} not found.")
        return

    user_data = user_response.json()
    employee_name = user_data.get("name")

    # Fetch TODO list data
    todos_response = requests.get(f"{base_url}/todos?userId={employee_id}")
    if todos_response.status_code != 200:
        print(f"Could not fetch TODO list for user ID {employee_id}.")
        return

    todos_data = todos_response.json()

    # Calculate the number of completed and total tasks
    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task.get("completed")]
    number_of_done_tasks = len(done_tasks)

    # Print the TODO list progress
    print(
        f"Employee {employee_name} is done with tasks("
        f"{number_of_done_tasks}/{total_tasks}):"
    )
    for task in done_tasks:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    get_employee_todo_progress(employee_id)
