'''

Name: Adam Webb and Adam Krisciunas
email: webb2at@mail.uc.edu, krisciag@mail.uc.edu
Assignment: Assignment 11
Course: IS 4010
Semester/Year: Fall 2022
Brief Description: Make an API call with a URL
Citations:

'''


#main

import json

import requests

response = requests.get('https://api.fda.gov/drug/event.json?limit=2&api_key=kOro3fDrczYqCaIuQ2PxC2B5DFpeSB9376Ytm5ot')
json_string = response.content
    
parsed_json = json.loads(json_string)    

#print(parsed_json['meta']['disclaimer']) Tested out printing meta and results data from the server. 

#print(parsed_json['results'][0]['safetyreportid'])

#print(parsed_json['meta'])

metaData = (parsed_json['meta'])
    
    
print('One drug adverse even report: Meta Data\n')

for meta, data in metaData.items():
    print(meta, ":", data)


#Adam Krisciunas Part

response = requests.get('https://v2.jokeapi.dev/joke/Any?safe-mode&amount=5')
json_string = response.content
    
parsed_json = json.loads(json_string) # Now we have a python dictionary

#print(parsed_json) - make sure it prints
#print(type(parsed_json)) - make sure its a dictionary

#part of the joke is that this code will sometimes run and sometimes not run. real funny if you ask me.
for i in range(4):
    print("your jokes sir: ", parsed_json['jokes'][i]['setup'], parsed_json['jokes'][i]['delivery'] )

