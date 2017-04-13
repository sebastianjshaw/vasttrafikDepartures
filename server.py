import requests # Used to get the URL responses.
import base64 # Used to encrypt the key and secret
import json # used to manipulate the returned JSON data
import time #used for getting the current time for the request.
from flask import Flask #import the flask webapp
from flask import render_template #import the flask webapp
import os #needed to set the timezone as pythonanywhere uses a different base zone.
import config

# Variables to filter
vTrack = 'A'
vBus = '16'
os.environ['TZ'] = 'Europe/Oslo'
time.tzset()

app = Flask(__name__)

@app.route('/')
def index(name=None):

	def authorize( ):
	# authorizes using the key and secret to get a valid token from vastraffik to authenticate with the API
	    
	    TOKEN_URL = 'https://api.vasttrafik.se/token' # URL to obtain the authentication token. Currently not used as we hardcode.
	    CONSUMER_KEY = config.CONSUMER_KEY # Key for getting an Authentication Token (auth_token)
	    CONSUMER_SECRET = config.CONSUMER_SECRET # Secret for getting an Authentication Token (auth_token)

	    data = {'grant_type': 'client_credentials'} #requred for the response to work.
	    auth_headers = {'Content-Type': 'application/x-www-form-urlencoded',
	    		'Authorization': 'Basic ' + base64.b64encode((CONSUMER_KEY + ':' + CONSUMER_SECRET).encode()).decode()} # header is what passes teh authentication string.
	    auth_r = requests.post(url=TOKEN_URL, data=data, headers=auth_headers) #response with the full request
	    token = json.loads(auth_r.content.decode('UTF-8')) #requesst is decoded as it is a JSON response
	    auth_token = token["access_token"] #the specific token is parameterized
	    return (auth_token); #function returns the token needed by the API

	def requestDepartures():
	#Function to request the departureinformation.
	    parameters = {'id': '9021014005465000', 'date': time.strftime("%Y-%m-%d"), 'time': time.strftime("%H:%M"), 'format': 'json'} # Defines the parameters to be passed in the URL
	    url = 'https://api.vasttrafik.se/bin/rest.exe/v2/departureBoard' # URL to the API
	    headers = {'Authorization':'Bearer '+auth_token} # API Headers to allow for access. Note there is no space before or after the : the documentation is incorrect here.
	    r = requests.get(url=url, params=parameters, headers=headers) # response is returned in variable r
	    return r; #r is returned to anything calling the function.

	while True:

		requestTime = time.strftime("%Y-%m-%d - %H:%M:%S")
		auth_token=authorize() #calls the authorize method and gets the token.
		r = requestDepartures() #calls the departure function
		json_results = json.loads(r.content.decode('UTF-8'), 'UTF-8') # This takes the request data (r) turns it into valid json and drops it into the json_results variable. (parameterised with variables for later abstraction)
		busFilter = [row for row in json_results["DepartureBoard"]["Departure"] if vBus == row["sname"] and vTrack == row["track"]] # This filters the json data and shows only vBus on vTrack
		firstBus = busFilter[0]['rtTime'] #takes the first result of the above filter and makes it a direct parameter
		secondBus = busFilter[1]['rtTime'] #takes the second result of the busFUlter and makes it a direct paramter
		return render_template('data.html', r=r, name=name, vBus=vBus, vTrack=vTrack, firstBus=firstBus, secondBus=secondBus, requestTime=requestTime) #returns all the relevant fields for the flask HTML file to render the information.
		time.sleep(120)	#sets the while look to sleep for 120 seconds before rerunning.

	else:
		print("There was an error with the application")



if __name__ == '__main__':
  app.run(debug=True)