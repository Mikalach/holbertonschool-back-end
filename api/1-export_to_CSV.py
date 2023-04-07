#!/usr/bin/python3
"""documented"""
import csv
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
    total_tasks = len(todo_list)
    done_tasks = sum(1 for task in todo_list if task["completed"])

    # Export data to CSV file
    with open(f"{employee_id}.csv", "w") as f:
        csv_writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in todo_list:

            csv_writer.writerow([employee_id, employee_name, task["completed"], task["title"]])

    print(f"Todo list exported to {employee_id}.csv")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: Employee ID is required.")
    else:
        get_employee_todo_progress(int(sys.argv[1]))
