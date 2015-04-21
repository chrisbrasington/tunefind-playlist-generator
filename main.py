import requests, pprint
from keys import api

def get(url):

	response = requests.get(url, auth=(api.username, api.password))
	data = response.json()

	pprint.pprint(data)

if __name__ == '__main__':

	print 'hello world'
	url = 'https://www.tunefind.com/api/v1/show/supernatural/season-1/5239'

	get(url)




