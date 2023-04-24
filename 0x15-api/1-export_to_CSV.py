#!/usr/bin/python3

"""Exports the to-do list information for a given employee ID to CSV format."""
import csv
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com"
    user = requests.get(f"{url}/users/{user_id}").json()
    username = user.get("username", "")

    todos = requests.get(f"{url}/todos", params={"userId": user_id}).json()

    with open(f"{user_id}.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        writer.writerow(["user_id", "username", "completed", "title"])

        for todo in todos:
            writer.writerow([
                user_id,
                username,
                todo.get("completed", False),
                todo.get("title", "")
            ])

