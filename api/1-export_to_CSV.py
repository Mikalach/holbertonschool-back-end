#!/usr/bin/python3
"""
Fetches todo list progress for a given employee ID from a REST API
and exports it to a CSV file
"""
import requests
import sys
import csv


def get_employee_todo_progress(employee_id):
    # Fetch employee name
    users_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(users_url)
    if response.status_code != 200:
        print("Error: Employee not found.")
        return

    employee_name = response.json()["name"]

    # Fetch todo list for the employee
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    query = {"userId": employee_id}
    response = requests.get(todos_url, params=query)
    if response.status_code != 200:
        print("Error: Todo list not found for the employee.")
        return

    todo_list = response.json()
    total_tasks = len(todo_list)
    done_tasks = sum(1 for task in todo_list if task["completed"])

    # Print output
    print(f"Employee {employee_name} is done with tasks"
          f"({done_tasks}/{total_tasks}):")
    for task in todo_list:
        task_title = f'"{task["title"]}"'
        task_status = str(task["completed"])
        print(f'"{employee_id}","{employee_name}","{task_status}","{task_title}"')

    # Export data to CSV file
    with open(f"{employee_id}.csv", "w") as f:
        f.write('"USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"\n')
        for task in todo_list:
            task_title = f'{task["title"]}'
            task_status = str(task["completed"])
            f.write(f'"{employee_id}","{employee_name}","{task_status}","{task_title}"\n')

    print(f"Todo list exported to {employee_id}.csv")
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: Employee ID is required.")
    else:
        get_employee_todo_progress(int(sys.argv[1]))
