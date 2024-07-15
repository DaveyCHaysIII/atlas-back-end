#!/usr/bin/python3
""" write a script that exports all users and todos to json"""
import json
import requests


def all_users_and_todos():
    """ Method exports all employee usernames and todo data to json file """

    base_url = 'https://jsonplaceholder.typicode.com'
    todo_url = f'{base_url}/todos'
    users_url = f'{base_url}/users'
    todos = requests.get(todo_url)
    users = requests.get(users_url)

    if todos.status_code != 200:
        print('Failed to fetch todos')
        return

    if users.status_code != 200:
        print('Failed to fetch usernames')
        return

    file_name = 'todo_all_employees.json'

    list = {}
    for user in users.json():
        user_id = user['id']
        user_name = user['username']
        todos_list = [todo for todo in todos.json()
                      if todo['userId'] == user_id]
        data = [{
            "username": user_name,
            "task": todo['title'],
            "completed": todo['completed']
        } for todo in todos_list]

        list[str(user_id)] = data

    # create file and write formatted data
    with open(file_name, 'w') as f:
        json.dump(list, f)


if __name__ == '__main__':
    all_users_and_todos()
