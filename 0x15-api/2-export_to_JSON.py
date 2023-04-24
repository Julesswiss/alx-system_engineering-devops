#!/usr/bin/python3
"""getting data from jsonplaceholder"""
import requests
import sys

if __name__ == '__main__':
    """REST API manipulations here"""
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

    with open("{}.json".format(employee_id), 'w') as f:
        f.write('{')
        f.write('"{}"'.format(employee_id))
        f.write(':[')
        for i, todo in enumerate(todo_response):
            task_status = todo.get("completed")
            task_title = todo.get("title")
            if i == len(todo_response) - 1:
                f.write(
                    '{{"task": "{}", "completed": {}, "username": "{}"}}'.
                    format(
                        task_title,
                        'true' if task_status else 'false',
                        username))
            else:
                f.write(
                    '{{"task": "{}", "completed": {}, "username": "{}"}}, '.
                    format(
                        task_title,
                        'true' if task_status else 'false',
                        username))

        f.write(']}')
