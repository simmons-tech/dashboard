from django.http import HttpResponse
import feedparser
import datetime
import lxml.html
import json
import parse
import dateutil.parser

def parse_menu( raw ):
	menu = {}

	# Keep track of the last dish we added so that we can go back and change it's description.
	last_dish = None
	for line in raw.replace(u'\xa0', '').split('\n'):

		# Just skip empty lines...
		if line is u'':
			continue

		result = parse.parse("[{1}] {2}", line)
	
		if result is not None:
			station = result[0].title()
			dish_name = result[1].title()
			if not station in menu:
				menu[ station ] = []
			dish = {"name":dish_name,"description":""}
			menu[ station ].append( dish )
			last_dish = dish
		elif last_dish:
			last_dish["description"] += line
	return menu

def menus_for_date( date ):
	# Make the URL and the Feed
	url = 'http://www.cafebonappetit.com/rss/menu/402'
	for raw_entry in feedparser.parse(url).entries:
		# Convert the title of the post, which contains a string date,
		# into an actual date object. Compare to see if we've got what we need.
		if date == dateutil.parser.parse( raw_entry.title_detail.value ).date():

			# First, split up the HTML on h3 tags, which represent meals...
			meals_data = raw_entry.summary.split("<h3>")
			meals = {}
			for meal in meals_data:
				if meal == u'':
					continue
				s = meal.split("</h3>")
				meal_name = s[0]
				meal_menu = s[1]

				parser = lxml.html.fromstring(meal_menu)
				textversion = lxml.html.tostring(parser, method='text', encoding=unicode)

				meal_menu = parse_menu(textversion)

				meals[ meal_name ] = {'menu':meal_menu}
			return {'meals':meals}

	# If we haven't found anything, we have no meals. :-( Return an empty structure.
	return {'meals':{}}
		
def getDiningMenu(request):
	today = datetime.datetime.now().date()
	payload = menus_for_date( today )

	return HttpResponse(json.dumps(payload), mimetype="application/json")
