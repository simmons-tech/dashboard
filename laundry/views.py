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
import lxml.html
import json

def laundry(request):
	lvs = lxml.html.parse('http://laundryview.com/lvs.php')
	div = lvs.find(".//div[@id='campus1']")
	rooms = []
	statuses = []
	for a in div.findall('.//a'):
		rooms.append(str(a.text).strip().title())
	for span in div.findall('.//span'):
		statuses.append(str(span.text).strip())

	pairs = dict(zip(rooms, statuses))

	def parseAvalibility( s ):
		return {'open_washers': s[1], 'open_dryers': s[7], 'total_washers':2, 'total_dryers':2}

	simmons = {}
	for room in rooms:
		if room.startswith('Simmons'):
			simmons[room[-3:]] = parseAvalibility( pairs[room] )

	payload = {'laundry': simmons}
	return HttpResponse(json.dumps(payload), content_type="application/json")
