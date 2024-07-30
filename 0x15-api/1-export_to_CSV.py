#!/usr/bin/python3
"""
This script fetches and displays the TODO list progress for a given employee ID
from a REST API and exports the data to a CSV file.

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
- Exports the TODO list data to a CSV file in the format:
    "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
  The file name must be: USER_ID.csv

Example usage:
    python3 1-export_to_CSV.py 2
"""

import csv
import requests as r
import sys

# Define base URL
BASE_URL = "https://jsonplaceholder.typicode.com/"


def get_user_data(user_id):
    """
    Fetch user data and TODO list for the given user ID.
    """
    user = r.get(f"{BASE_URL}users/{user_id}").json()
    username = user.get("username")
    todos = r.get(f"{BASE_URL}todos", params={"userId": user_id}).json()
    return user_id, username, todos


def export_to_csv(filename, data):
    """
    Export data to a CSV file with the specified filename.
    """
    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for element in data:
            writer.writerow(element)


def main():
    """
    Main function to handle user input and process the TODO list.
    """
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    try:
        user_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    # Get user data
    user_id, username, todo_data = get_user_data(user_id)

    # Prepare data for CSV export
    csv_data = [
        [user_id, username, task.get("completed"), task.get("title")]
        for task in todo_data
    ]

    # Export data to CSV
    export_to_csv(f"{user_id}.csv", csv_data)
    print(f"Data for employee ID {user_id} has been exported to {user_id}.csv")


if __name__ == "__main__":
    main()
