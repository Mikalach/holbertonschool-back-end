#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
import sys


if __name__ == "__main__":
    # Check for correct number of arguments
    if len(sys.argv) != 2:
        print("Usage: {} employee_id".format(sys.argv[0]))
        sys.exit(1)

    # Get employee ID from command line argument
    employee_id = sys.argv[1]

    # Get employee name from API
    url_user = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    response_user = requests.get(url_user)
    if response_user.status_code != 200:
        print("Error: Employee ID not found")
        sys.exit(1)
    employee_name = response_user.json().get("name")

    # Get employee's TODO list from API
    url_todos = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)
    response_todos = requests.get(url_todos)
    if response_todos.status_code != 200:
        print("Error: Something went wrong")
        sys.exit(1)
    todos = response_todos.json()

    # Process TODO list and display progress
    total_tasks = len(todos)
    completed_tasks = [t for t in todos if t.get("completed")]
    num_completed_tasks = len(completed_tasks)
    print("Employee {} is done with tasks({}/{}):".format(employee_name, num_completed_tasks, total_tasks))
    for task in completed_tasks:
        print("\t {}".format(task.get("title")))
