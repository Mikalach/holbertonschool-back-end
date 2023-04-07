#!/usr/bin/python3
"""documented"""
import json
import requests
import sys


def get_employee_todo_progress(employee_id):
    # Fetch employee name
    users_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(users_url)
    employee_name = response.json()["username"]

    # Fetch todo list for the employee
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    query = {"userId": employee_id}
    response = requests.get(todos_url, params=query)

    todo_list = response.json()
    tasks = []
    for task in todo_list:
        task_data = {"task": task["title"], "completed": task["completed"],
                     "username": employee_name}
        tasks.append(task_data)

    # Export data to CSV file
    with open(f"{employee_id}.json", "w") as f:
        json.dump({employee_id: tasks}, f)

    print(f"Todo list exported to {employee_id}.json")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: Employee ID is required.")
    else:
        get_employee_todo_progress(int(sys.argv[1]))
