from django.http import HttpResponse
from django.shortcuts import render_to_response
import json
import feedparser

def getEvents(request):
    # parsed events list
    events = []
    
    def formatEventsDate(item):
        # Only need to return hour in string format
        if item.tm_hour < 12:
            am_pm = 'AM'
        else:
            am_pm = 'PM'
        hour = item.tm_hour % 12
        return "{} {}".format(hour, am_pm)

    try:
        # create custom rss from http://events.mit.edu/rsssearch.html
        url = "http://events.mit.edu/rss"
        d = feedparser.parse(url)

        for entry in d.entries:
            event = {'title': entry.title,
                     'description': entry.summary,
                     'time': formatEventsDate(entry.updated_parsed),}

        events.append(event)

    except:
        event = {'title': 'Unavailable',
                 'description': 'Unavailable',
                 'time': 'NA',}
        events.append(event)
        
        
    jsonout = json.dumps(events, indent=4)
    return HttpResponse(jsonout, mimetype="application/json")
