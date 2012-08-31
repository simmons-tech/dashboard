Simmons Hall Dashboard
=========
# Introduction
This project is a redesign of the simmonsdash project. The goal is to
create an expandable and easy to deploy dashboard for the Simmons Hall
ground floor monitors.

# Applications
## Events
The events app provides a daily events calendar. The MIT RSS feed is parsed and is available at /events. Each event object has a title, description, and time. 

## Nextbus
For information on the Nextbus api visit http://www.nextbus.com/xmlFeedDocs/NextBusXMLFeed.pdf. The code was copied from the Nextbus code used in the Dormbase project. It has been lightly modified.

The next 3 shuttles can be accessed from /nextbus. It will return a json object with shuttle, next, second, third, as seen below:

{"shuttle": "Saferide Cambridge West", "second": "41", "third": "71", "next": "11"}