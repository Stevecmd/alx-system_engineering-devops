#!/usr/bin/python3

"""
Fetches and records all tasks from a specific employee
from a REST API and exports the data to a JSON file.
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
