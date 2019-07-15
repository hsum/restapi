#!/usr/bin/env python
'''
Receive an API request over HTTP.
Parse the request and assemble an appropriate response.
Manipulate and parse JSON string data.
'''

import json
import requests
import pprint
import collections


if __name__ == '__main__':
    #Receive an API request over HTTP.
    response = requests.get("https://jsonplaceholder.typicode.com/todos")

    #Parse the request and assemble an appropriate response.
    todos = json.loads(response.text)
    number_of_todos = len(todos)
    print(f'{number_of_todos} todos loaded')
    priority_todos = todos[:10]
    print('')
    print('top 10 priority todos:')
    pprint.pprint(priority_todos)

    user_counter = collections.Counter(todo['userId'] for todo in todos)
    print(user_counter)
