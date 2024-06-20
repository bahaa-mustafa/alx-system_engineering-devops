#!/usr/bin/python3
# using REST API as a python script for employee ID
# to return information about todo list progress

import requests
from sys import argv


if __name__ == "__main__":
    # check if id is found in command line arguments
    if len(argv) != 2:
        exit(1)

    employee_id = argv[1]
    jason_placeholder = "https://jsonplaceholder.typicode.com/users"
    url = f'{jason_placeholder}/{employee_id}'

    # GET request to API
    respose = requests.get(url)

    # check successful of request
    if respose.status_code == 200:
        employee_name = respose.json().get('name')
        todo_url = f'{url}/todos'
        result = requests.get(todo_url)
        tasks = result.json()

        # filter complete tasks
        task_done = [tasks for task in tasks if task.get('completed')]

        # display progress of todo list
        print("Employee {} is done with tasks({}/{}):".format(employee_name, len(task_done), len(tasks)))
        for task in task_done:
            print("\t{}".format(task.get('title')))
        
    else:
        # display Error in fail of reqest
        print("Error: Unable to fetch data. Status code: {}".format(respose.status_code))
