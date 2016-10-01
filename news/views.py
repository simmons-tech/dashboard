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
import json
import feedparser
from random import choice

def getTopStories(request):
    # Chose BBC for now, but should include others in the future
    # Consider adding stock ticker here too
    bbcWorldRSS = 'http://newsrss.bbc.co.uk/rss/newsonline_world_edition/front_page/rss.xml'

    # News array
    news = []
    for entry in feedparser.parse(bbcWorldRSS).entries:
        story = { 'title': entry.title,
                  'summary': entry.summary,}
        news.append(story)

    jsonout = json.dumps(choice(news))
    
    return HttpResponse(jsonout, content_type="application/json")
