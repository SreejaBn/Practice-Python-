import json
import requests

city_name= str(input('Enter the name of the city: '))

api_key= 'eb32f8e1b7122b90618e1429ee0e20f0'
api= f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'

server_info= requests.get(api) #data getting fetched

data= server_info.json() #data converted into json

preety= json.dumps(data, indent= '\t') #converts the data into string and puts indentation

# to fetch a specific data from json
description= data['weather'][0]['description'] #0 is put here to fetch the first data from weather. then, I wanted description to be displayed specificly, so I wrote description in the second[]

temp= data['main']['temp'] #I am not writing [0] because main is not a list. a list can be identified, if it's written inside []
print(f'The current weather description is: {description} and the current temperature is: {temp}')