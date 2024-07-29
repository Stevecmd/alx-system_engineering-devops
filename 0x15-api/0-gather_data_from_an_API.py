#!/usr/bin/python3
"""
This script fetches and displays the TODO list progress for a given employee ID
from a REST API.

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

Example usage:
    python3 0-gather_data_from_an_API.py 2
"""

import requests as r
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/"

    try:
        user_response = r.get(f"{base_url}users/{employee_id}")
        user_response.raise_for_status()
        user = user_response.json()

        todos_response = r.get(
            f"{base_url}todos",
            params={"userId": employee_id}
        )
        todos_response.raise_for_status()
        todos = todos_response.json()
    except r.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)

    completed_tasks = [
        task.get("title")
        for task in todos
        if task.get("completed")
    ]

    employee_name = user.get("name")
    num_completed_tasks = len(completed_tasks)
    total_tasks = len(todos)

    print(
        f"Employee {employee_name} "
        f"is done with tasks("
        f"{num_completed_tasks}/{total_tasks}):"
    )
    for task in completed_tasks:
        print(f"\t {task}")
