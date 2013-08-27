from django.http import HttpResponse
from lxml import etree
import json

def getArrival(request):
	# Nextbus api: http://www.nextbus.com/xmlFeedDocs/NextBusXMLFeed.pdf
	baseURL = 'http://webservices.nextbus.com/service/publicXMLFeed?command=predictions'
	agency = 'mit'
	stop = 'simmhl'

	techURL = '{}&a={}&r={}&s={}'.format(baseURL, agency, 'tech', stop)
	saferideURL = '{}&a={}&r={}&s={}'.format(baseURL, agency, 'saferidecambwest', stop)

	try:
		techTimes = etree.parse(techURL).findall('predictions/direction/prediction')
		saferideTimes = etree.parse(saferideURL).findall('predictions/direction/prediction')
	except:
		techTimes = []
		saferideTimes = []

	times = []

	def nextbus( name, time_till ):
		return {'name':name,'time_till':time_till}

	for bus in techTimes:
		times.append( nextbus( "Tech Shuttle", bus.get('minutes') ) )
	for bus in saferideTimes:
		times.append( nextbus( "Saferide Cambridge West", bus.get('minutes') ) )

	#TODO: Sort times by time_till

	return HttpResponse(json.dumps({'buses': times}), mimetype="application/json")
