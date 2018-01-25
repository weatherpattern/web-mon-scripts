import requests

# Query the web monitoring API to get random links
# Integer -> List
def query_webmondb():
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
	return time

# Check to see latest time is within the time limit
# Int, DateTime -> Boolean
def check_time(time_limit, time):
	return status

# Take Respones from Wayback and determine if the IA has recent snapshots
# Dict -> None
def is_healthy(responses):
	link_health = [get_time(response) for response in responses]
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
links = query_webmondb()
responses = [query_wayback(url) for url in links]
is_healthy(responses)




