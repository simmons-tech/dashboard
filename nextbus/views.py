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

    techTimes = etree.parse(techURL).findall('predictions/direction/prediction')
    saferideTimes = etree.parse(saferideURL).findall('predictions/direction/prediction')

    # If techTimes is empty, then it isn't running, so check Saferide
    if techTimes:
        times = [i.get('minutes') for i in techTimes]
        title = 'Tech Shuttle'
    elif saferideTimes:
        times =  [i.get('minutes') for i in saferideTimes]
        title = 'Saferide Cambridge West'
    else:
        # Fake times for testing
        times = ['5', '12', '21']
        title = 'Unavailable'
        
    out = {'title': title,
           'next': times[0],
           'second': times[1],
           'third': times[2]}
    
    return HttpResponse(json.dumps(out), mimetype="application/json")

