#!/usr/bin/python3
"""write a script to write data to a CSV from an api"""

import csv
import requests
import sys


def get_employee_prog_csv(employee_id):
    """function gets data from API of a given employee ID"""
    base_url = "https://jsonplaceholder.typicode.com"

    todo_url = f'{base_url}/todos?userId={employee_id}'
    user_url = f'{base_url}/users?id={employee_id}'
    response1 = requests.get(todo_url)
    response2 = requests.get(user_url)

    if response1.status_code != 200:
        print(f'Failed to fetch todos for employee ID {employee_id}.')
        return

    if response2.status_code != 200:
        print(f'Failed to fetch name for employee ID {employee_id}.')
        return

    todos = response1.json()
    user_name = response2.json()[0]['username']
    file_name = f'{employee_id}.csv'

    with open(file_name, mode='w', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                employee_id, user_name,
                task['completed'], task['title']])


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
