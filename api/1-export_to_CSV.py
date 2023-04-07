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
    username = response.json()["username"]

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

    # Export to CSV
    filename = f"{employee_id}.csv"
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in todo_list:
            task_completed_status = "Complete" if task["completed"] else "Incomplete"
            task_title = task["title"]
            writer.writerow([employee_id, username, task_completed_status, task_title])

    # Print output
    print(f"Employee {employee_name} is done with tasks"
          f"({done_tasks}/{total_tasks}). Exported to {filename}.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: Employee ID is required.")
    else:
        get_employee_todo_progress(int(sys.argv[1]))
