import requests


fileoutput = open("ia_healthcheck.txt","w")

links = ['http://archive.org/wayback/available?url=epa.gov',
	'http://archive.org/wayback/available?url=energy.gov',
	'http://archive.org/wayback/available?url=doi.gov',
	'http://archive.org/wayback/available?url=usda.gov',
	'http://archive.org/wayback/available?url=noaa.gov']

for url in links:

	
	ia_info = requests.get(url)
	print(ia_info.content)

	fileoutput.write('\n URL: \n')
	fileoutput.write(str(ia_info.content))
	

fileoutput.close()