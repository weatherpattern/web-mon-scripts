import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime, timedelta
import os


MAX_CAPTURE_AGE = timedelta(hours=72)
SCANNER_USER = os.environ['SCANNER_USER']
SCANNER_PASSWORD = os.environ['SCANNER_PASSWORD']

# Query the web monitoring API to get random links
# Integer -> List
def query_webmondb():
	"""
	Set user and pass as environmental variables from command line
	For MacOS: in the terminal:
	export SCANNER_USER="your API user name"
	export SCANNER_PASSWORD="your API password"
	"""
	api = 'https://api.monitoring.envirodatagov.org/api/v0/pages?chunk_size=1'
	response = requests.get(api, auth=HTTPBasicAuth(SCANNER_USER, SCANNER_PASSWORD))
	response = response.json()

	print(response)
	#	fileoutput = open("api_pages.txt", "w")
	#	fileoutput.write('API Response content: \n')
	#	fileoutput.write(str(response.content))
	#	fileoutput.close()	
	links = [
		'epa.gov',
		'energy.gov',
		'doi.gov',
		'usda.gov',
		'noaa.gov'
	]	
	return links

def query_wayback(url):
	"""
	Query Wayback Machine
	String -> JSON Object
	""" 
	url = 'http://archive.org/wayback/available?url=%s' % url
	response = requests.get(url)
	response = response.json()
	return response


def get_time(response):
	"""
	Get the timestamp from the Wayback URL JSON Object
	Convert Wayback time to datetime object
	JSON Object -> DateTime Object
	"""
	time = response['archived_snapshots']['closest']['timestamp']
	return datetime.strptime(time, '%Y%m%d%H%M%S')

def check_time(time_limit, response):
	"""
	Check to see latest time is within the time limit
	Int, DateTime -> Boolean
	"""
	time = get_time(response)
	status = (datetime.now() - time)  < time_limit
	return {'Status': status, 'Response': response, 'Current Time': datetime.now(), 'Last Capture': time}

def is_healthy(responses):
	"""
	Take Respones from Wayback and determine if the IA has recent snapshots
	Dict -> None
	"""
	link_health = [check_time(MAX_CAPTURE_AGE, response) for response in responses]
	output_file(link_health)
	return	


def output_file(responses):
	"""
	Write Output to a Text file
	List -> None
	"""
	fileoutput = open("ia_healthcheck.txt", "w")

	for url in responses:
		fileoutput.write(str(url)+'\n\n\n')		

	fileoutput.close()

	return


def output_email():
	"""
	Send Output to and Email
	List -> None
	"""
	return

# Get the random list of links from the Web Monitoring DB
# Get the responses of the links from the Wayback URL
# Check to see if the responses are within the time limit and write the output
if  __name__ == "__main__":
	links = query_webmondb()
	responses = [query_wayback(url) for url in links]
	is_healthy(responses)




