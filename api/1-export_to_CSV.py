#!/usr/bin/python3
"""write a script to write data to a CSV from an api"""

import csv
import requests
import sys


def get_employee_prog_csv(employee_id):
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
    csv_filename = f"{employee_id}.csv"
    with open(csv_filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todos:
            csv_writer.writerow([employee_id,
                                employee_name,
                                task['completed'],
                                task['title']])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    get_employee_prog_csv(employee_id)
