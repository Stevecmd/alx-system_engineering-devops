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


def fetch_data(employee_id):
    base_url = "https://jsonplaceholder.typicode.com/"
    try:
        employee_info = r.get(f"{base_url}users/{employee_id}").json()
        tasks = r.get(
            f"{base_url}todos",
            params={"userId": employee_id}
        ).json()
    except r.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)
    return employee_info, tasks


def main(employee_id):
    employee_info, tasks = fetch_data(employee_id)

    completed_tasks = [t["title"] for t in tasks if t["completed"]]

    employee_name = employee_info.get("name")
    num_completed = len(completed_tasks)
    num_tasks = len(tasks)

    print(
        f"Employee {employee_name} is done with tasks ("
        f"{num_completed}/{num_tasks}):"
    )
    for task in completed_tasks:
        # print(f"     {task}")
        print(f"\t {task}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer.")
        sys.exit(1)

    main(employee_id)
