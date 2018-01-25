import requests

def query_webmondb():
	links = [
		'epa.gov',
		'energy.gov',
		'doi.gov',
		'usda.gov',
		'noaa.gov'
	]	
	return links

def query_wayback(url):
	url = 'http://archive.org/wayback/available?url=%s' % url
	response = requests.get(url)
	response = response.json()
	return response

def get_time(response):
	time = response['archived_snapshots']['closest']['timestamp']

	print(time)
	return time

def check_time(time):
	return status

def is_healthy(responses):
	link_health = [get_time(response) for response in responses]
	output_file(link_health)
	return	

def output_file(responses):
	fileoutput = open("ia_healthcheck.txt", "w")

	for url in responses:
		fileoutput.write('\n URL: \n')
		fileoutput.write(str(url))		

	fileoutput.close()

	return

def output_email():
	return

links = query_webmondb()
responses = [query_wayback(url) for url in links]
is_healthy(responses)




