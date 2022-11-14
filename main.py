'''

Name: Adam Webb
email: webb2at@mail.uc.edu
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


