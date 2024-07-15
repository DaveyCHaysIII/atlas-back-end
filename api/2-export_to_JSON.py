#!/usr/bin/python3
"""write a script that exports JSON data from an api"""
import json
import sys
import urllib.request


def get_employee_todo_progress(employee_id):
    """retrieve data from API and spit out JSON"""
    base_url = "https://jsonplaceholder.typicode.com/"
    employee_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/todos?userId={employee_id}"

    with urllib.request.urlopen(employee_url) as response:
        employee_info = response.read()
    employee_info = json.loads(employee_info)

    with urllib.request.urlopen(todo_url) as response:
        todo_list = response.read()
    todo_list = json.loads(todo_list)
    user_id = employee_info['id']

    completed_tasks = []
    for todo in todo_list:
        completed_tasks.append({
            "task": todo["title"],
            "completed": todo["completed"],
            "username": employee_info["username"]
        })

    output_data = {str(user_id): completed_tasks}

    filename = f"{user_id}.json"
    with open(filename, 'w') as json_file:
        json.dump(output_data, json_file, indent=4)

    print(f"Data exported to {filename}")


if __name__ == "__main__":
    get_employee_todo_progress(int(sys.argv[1]))