#!/usr/bin/python3
"""write a script to gather data from an api"""

import requests
import sys


def get_employee_prog(employee_id):
    """function gets data from API of a given employee ID"""
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch employee details
    employee_data = requests.get(f"{base_url}/users/{employee_id}")
    if employee_data.status_code != 200:
        print("Failed to fetch employee details")
        return

    employee = employee_data.json()
    employee_name = employee['name']

    todos_data = requests.get(f"{base_url}/todos",
                              params={'userId': employee_id})
    if todos_data.status_code != 200:
        print("Failed to fetch TODO list")
        return

    todos = todos_data.json()
    total_tasks = len(todos)
    finished_tasks = [task for task in todos if task['completed']]
    number_finished_tasks = len(finished_tasks)

    print(f"Employee {employee_name}" 
          + "is done with tasks({number_finished_tasks}/{total_tasks}):")
    for task in finished_tasks:
        print(f"\t {task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    get_employee_prog(employee_id)
