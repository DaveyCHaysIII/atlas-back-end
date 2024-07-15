#!/usr/bin/python3
"""write a script that creates a dictionary of a list of dictionaries
based on JSON data from an API"""

import json
import requests
import sys


def get_all_employees_todo_progress():
    # Base URLs for the API
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch all employees
    employees_response = requests.get(f"{base_url}/users")
    if employees_response.status_code != 200:
        print("Failed to fetch employees")
        return

    employees = employees_response.json()

    # Dictionary to hold all tasks
    all_tasks = {}

    for employee in employees:
        employee_id = employee['id']
        employee_name = employee['name']

        # Fetch TODO list for the employee
        todos_response = requests.get(f"{base_url}/todos",
                                      params={'userId': employee_id})
        if todos_response.status_code != 200:
            print(f"Failed to fetch TODO list for employee {employee_id}")
            continue

        todos = todos_response.json()

        # Collect tasks for this employee
        employee_tasks = []
        for task in todos:
            employee_tasks.append({
                "username": employee_name,
                "task": task['title'],
                "completed": task['completed']
            })

        # Add to the all_tasks dictionary
        all_tasks[str(employee_id)] = employee_tasks

    # Export data to JSON
    json_filename = "todo_all_employees.json"
    with open(json_filename, mode='w') as json_file:
        json.dump(all_tasks, json_file, indent=4)

    print(f"Data exported to {json_filename}")


if __name__ == "__main__":
    if len(sys.argv) != 1:
        print("Usage: python script.py")
        sys.exit(1)

    get_all_employees_todo_progress()
