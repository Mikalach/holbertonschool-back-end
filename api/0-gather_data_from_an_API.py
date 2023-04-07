#!/usr/bin/python3
"""
Fetches todo list progress for a given employee ID from a REST API
"""

import requests
import sys


def get_employee_info(employee_id):
    """Returns employee's todo list progress"""

    # Fetch user name
    users_url = "https://jsonplaceholder.typicode.com/users"
    resp = requests.get(users_url).json()
    name = None
    for user in resp:
        if user['id'] == employee_id:
            name = user['name']
            break

    if not name:
        print("Employee not found.")
        return

    # Fetch todos for the user
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    params = {'userId': employee_id}
    resp = requests.get(todos_url, params=params).json()

    # Parse todo list and count completed tasks
    completed_tasks = []
    for todo in resp:
        if todo['completed']:
            completed_tasks.append(todo['title'])

    num_completed_tasks = len(completed_tasks)
    num_total_tasks = len(resp)

    # Print output
    print(f"Employee {name} is done with tasks({num_completed_tasks}/{num_total_tasks}):")
    for task in completed_tasks:
        print(f"\t{task}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python todo.py EMPLOYEE_ID")
    else:
        get_employee_info(int(sys.argv[1]))
