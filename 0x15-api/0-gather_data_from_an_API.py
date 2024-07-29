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
    base_url = "https://jsonplaceholder.typicode.com/"
    employee_id = sys.argv[1]

    # Fetch user information
    employee_info = r.get(
        base_url + "users/{}".format(employee_id)
    ).json()

    # Fetch tasks for the user
    tasks = r.get(
        base_url + "todos",
        params={"userId": employee_id}
    ).json()

    # Filter completed tasks
    completed_tasks = [
        t.get("title") for t in tasks if t.get("completed") is True
    ]

    # Get employee name
    employee_name = employee_info.get("name")

    # Count completed and total tasks
    num_completed = len(completed_tasks)
    num_tasks = len(tasks)

    # Print the tasks in the desired format
    print(f"Employee {employee_name} is done with tasks "
          f"({num_completed}/{num_tasks}):")
    [print(f"\t {task}") for task in completed_tasks]
