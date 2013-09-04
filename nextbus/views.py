### About #####################################################################
#                                                                             #
# This code is part of the Simmons Hall Dashboard project. An up-to-date      #
# version can be found at https://github.com/simmons-tech/dashboard .         #
#                                                                             #
# The project is built an maintained by Simmons Tech, a student organization  #
# at MIT. The original code was produced by Luke O'Malley '14 and             #
# Will Oursler '15                                                            #
#                                                                             #
### License and Warranty ######################################################
#                                                                             #
# Copyright 2013 Simmons Hall                                                 #
#                                                                             #
# Licensed under LGPL3 (the "License"). You may not use this work except in   #
# compliance with the License. You may obtain a copy of the License at        #
# http://opensource.org/licenses/lgpl-3.0.html .                              #
#                                                                             #
# Unless required by applicable law or agreed to in writing, software         #
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT   #
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.            #
###############################################################################

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

	times = sorted( times, key=lambda nb: nb['time_till'] )

	return HttpResponse(json.dumps({'buses': times}), mimetype="application/json")
