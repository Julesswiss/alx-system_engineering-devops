#!/usr/bin/python3
"""this gets data from json placeholder"""
import requests
import sys

if __name__ == '__main__':
    """REST API manipulations"""
    if len(sys.argv) > 1 and isinstance(eval(sys.argv[1]), int):
        pass
    else:
        sys.exit(0)

    BASE_API = "https://jsonplaceholder.typicode.com/"
    employee_id = sys.argv[1]
    user_response_url = BASE_API + "users/{}".format(employee_id)
    todo_response_url = BASE_API + "users/{}/todos".format(employee_id)

    user_response = requests.get(user_response_url).json()
    todo_response = requests.get(todo_response_url).json()

    employee_name = user_response.get('name')
    username = user_response.get('username')

    with open("{}.csv".format(employee_id), 'w') as f:
        for todo in todo_response:
            task_status = todo.get("completed")
            task_title = todo.get("title")
            to_write = '"{}","{}","{}","{}"\n'.format(
                employee_id, username, task_status, task_title)
            f.write(to_write)
