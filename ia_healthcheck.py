import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime, timedelta

# Query the web monitoring API to get random links
# Integer -> List
def query_webmondb():
	# Set user and pass as environmental variables from command line
	#api = 'https://api.monitoring.envirodatagov.org/api/v0/versions?chunk_size=1000'
	#response = requests.get(api, auth=HTTPBasicAuth('user', 'pass'))
	#response = response.json()

	#fileoutput = open("api_pages.txt", "w")
	#fileoutput.write('API Response content: \n')
	#fileoutput.write(str(response.content))
	#fileoutput.close()
	links = [
		'epa.gov',
		'energy.gov',
		'doi.gov',
		'usda.gov',
		'noaa.gov'
	]	
	return links

# Query Wayback Machine
# String -> JSON Object 
def query_wayback(url):
	url = 'http://archive.org/wayback/available?url=%s' % url
	response = requests.get(url)
	response = response.json()
	return response

# Get the timestamp from the Wayback URL JSON Object
# JSON Object -> DateTime Object
def get_time(response):
	time = response['archived_snapshots']['closest']['timestamp']
	time = str_to_datetime(time)
	return time

# Convert Wayback time to datetime object
# Str -> Datetime
def str_to_datetime(str):
	pydatetime = datetime.strptime(str, '%Y%m%d%H%M%S')
	return pydatetime

# Convert str to datetime hr object
# Str -> Datetime
def str_to_datetime_hr(str):
	pydatetime = datetime.strptime(str, '%H')
	return pydatetime

# Check to see latest time is within the time limit
# Int, DateTime -> Boolean
def check_time(time_limit, time):
	time = get_time(time)
	if (datetime.now() - time)  < time_limit:
		status = [True,datetime.now(),time]
	else:
		status = [False,datetime.now(),time]
	return status

# Take Respones from Wayback and determine if the IA has recent snapshots
# Dict -> None
def is_healthy(responses):
	link_health = [check_time(time_check, response) for response in responses]
	output_file(link_health)
	return	

# Write Output to a Text file
# List -> None
def output_file(responses):
	fileoutput = open("ia_healthcheck.txt", "w")

	for url in responses:
		fileoutput.write('\n URL: \n')
		fileoutput.write(str(url))		

	fileoutput.close()

	return

# Send Output to and Email
# List -> None
def output_email():
	return

# Get the random list of links from the Web Monitoring DB
# Get the responses of the links from the Wayback URL
# Check to see if the responses are within the time limit and write the output
time_check = timedelta(hours=72)
links = query_webmondb()
responses = [query_wayback(url) for url in links]
is_healthy(responses)




