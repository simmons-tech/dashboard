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
	return HttpResponse(json.dumps(payload), mimetype="application/json")
