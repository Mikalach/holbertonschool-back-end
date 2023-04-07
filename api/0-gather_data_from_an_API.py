#!/usr/bin/python3
"""
Fetches todo list progress for a given employee ID from a REST API
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./todo.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    # Fetch user information
    user = None
    resp = requests.get(users_url, params={"id": employee_id})
    if resp.ok:
        user = resp.json()[0]

    if not user:
        print("Employee not found")
        sys.exit(1)

    # Fetch user's TODO list
    todos = []
    resp = requests.get(todos_url, params={"userId": employee_id})
    if resp.ok:
        todos = resp.json()

    total_tasks = len(todos)
    done_tasks = sum(1 for todo in todos if todo["completed"])
    task_titles = [todo["title"] for todo in todos if todo["completed"]]

    # Print output
    print("Employee {} is done with tasks({}/{}):".format(
        user["name"], done_tasks, total_tasks))
    for title in task_titles:
        print("\t {}".format(title))
