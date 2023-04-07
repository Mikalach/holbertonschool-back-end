#!/usr/bin/python3
"""documented"""
import csv
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

    # Export data to CSV file
    with open(f"{employee_id}.csv", "w") as f:
        csv_writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in todo_list:
            csv_writer.writerow([employee_id, employee_name,
                                 task["completed"], task["title"]])

    return todo_list, employee_name


if __name__ == "__main__":
    all_todo_data = {}

    for employee_id in range(1, 11):
        todo_list, employee_name = get_employee_todo_progress(employee_id)
        all_todo_data[employee_id] = []
        for task in todo_list:
            all_todo_data[employee_id].append(
                {"username": employee_name,
                 "task": task["title"],
                 "completed": task["completed"]}
            )

    with open("todo_all_employees.json", "w") as f:
        json.dump(all_todo_data, f)

