# This program will show the people who are in space right now

import requests

people = requests.get('http://api.open-notify.org/astros.json')
json = people.json() 

print('The people currently in space are:')
for person in json['people']:
    print(person['name'])