import json
with open('user.json') as data_file:    
    data = json.load(data_file)

user = data['users']

for user in data:
  print("users full name is " + user['firstName'] + ' ' + user['lastName'])
  counter = 0
  while counter < len(user['details']):
    print("users mobile number is " + user['details'][counter]['mobileNo'])
    print("users age  is " + user['details'][counter]['age'])
    print("users city is " + user['details'][counter]['city'])
    counter = counter + 1
