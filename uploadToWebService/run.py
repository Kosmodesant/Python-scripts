import os
import requests

path = '/data/feedback/'
link = 'http://<External-IP-Address>/feedback/'
files = os.listdir(path)

for file in files:
        #Open files and process data within
        Data = open(path + file)
        iData = Data.read().split('\n')

        #Create dictionary of the retreaved data
        Dictionary = {"title":iData[0], "name":iData[1], "date":iData[2], "feedback":iData[3]}

        #Upload the feedback to the website
        response = requests.post(link, json=Dictionary)

        #Close the files
        Data.close()

print(response.status_code)
