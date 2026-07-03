#!/usr/bin/env python3

import json
import requests


def separate_tasks(tasks):
    completed = []
    incomplete = []
    for task in tasks:
        if task["completed"]:
            completed.append(task)
        else:
            incomplete.append(task)

    return completed, incomplete


def write_data(file_name, data):
    with open(file_name, "w") as out:
        json.dump(data, out, separators=(',', ':'))


def main():
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.content.decode())
        done, todo = separate_tasks(data)
        write_data("11-json/tasks_done.json", done)
        write_data("11-json/tasks_todo.json", todo)
    else:
        print("response status:", response.status_code)

    finished = len(done)
    print(f"{finished} of {finished + len(todo)} tarefas concluidas")


if __name__ == "__main__":
    main()
