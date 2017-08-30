#!/usr/bin/env python3

import requests
import json

if __name__ == '__main__':
    r = requests.get('http://localhost:5000/todo/api/v1.0/tasks')
    print(r.text)

    print("--------------------")

    url = 'http://localhost:5000/todo/api/v1.0/tasks'
    payload = {'title': 'Read a blog'}

    r = requests.post(url, json=payload)
    print(r.text)
