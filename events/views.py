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
from django.shortcuts import render_to_response
import json
import feedparser
from random import choice

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

    random_event =  choice(events)
        
    jsonout = json.dumps(random_event, indent=4)
    return HttpResponse(jsonout, content_type="application/json")
