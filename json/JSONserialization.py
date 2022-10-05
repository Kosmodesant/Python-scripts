# to JSON
import json

people = [
  {
    "name": "John Doe",
    "username": "Jdoe",
    "phone": {
      "office": "123-456-780",
      "cell": "987-654-321"
    },
    "department": "IT",
    "role": "software engineer"
  },
  {
    "name": "Tom Cruise",
    "username": "Tcruise",
    "phone": {
      "office": "777-777-777"
    },
    "department": "actors",
    "role": "unicorn"
  }
]

with open('people.json', 'w') as people_json:
    json.dump(people, people_json)
    
  
# from JSON  
import json
with open('people.json', 'r') as people_json:
  people = json.load(people_json)
  print(people)
