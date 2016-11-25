import requests 
import datetime 
import time 
from datetime import datetime, date, time
import urllib2
import json
import time as time_ 
 
loc_api = '7f4c231b1577732d1137264d4a63'		

today = int(round(time_.time() * 1000))
		
def a_search(query):
	api_key = loc_api
	url1 = 'https://api.meetup.com/2/open_events?&sign=true&photo-host=public&lat=51.513191&topic=' + query	
	a = query.replace(' ', '%20')
	final_url = url1 + '&lon=-0.133495&radius=10&key=' + api_key
	json_obj = urllib2.urlopen(final_url)
	data = json.load(json_obj)
	
	f = open('html_text.html', 'w')	

	f.write('<html><head>    <meta charset="utf-8" />    <title>Information</title></head>')
	f.write('<body>')
	for item in data['results']:
		if (int(item['time']) < today + 604800000): 
			f.write('<p>Name of group: ')
			f.write(str(item['group']['name']))
			f.write('</p><p>Name of event: ')
			f.write(str(item['name'])) 
			f.write('</p><p>Date: ')
			f.write(str(datetime.utcfromtimestamp(int(str(item['time']))/1000)))
			f.write('</p><p>Description: ')
			f.write(str(item['description']))
			f.write('</p><p></p>')
	f.write('</body></html>')
	f.close()
	
		
a_search('python')		







		