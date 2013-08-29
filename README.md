Simmons Hall Dashboard
=========

# Introduction
This project is a reborn simmonsdash. The goal is to create a maintainable and expandable dashboard system for Simmons Hall. We are making the code as generic as possible so that it's usable by others. One of the main goals is to make the code accessible to future students and Simmons Tech members. We are doing our best to document our process and methodology so that anyone can pick up where we left off. If you have any questions about the project or want to contribute please contact us at simmons-tech@mit.edu. 

# Architecture
The back-end is written in Django and the front-end is HTML5 and Javascript. The Javascript is written in CoffeeScript. The intent was to make the project as pythonic as possible because of MIT's focus on the language. We hope this makes the project more accessible to you. 

Each widget on the dashboard is its own application. Each application is responsible for supplying its own static files, urls, and views. Each application should be standalone. Widget HTML code is currently added to the dashboard/templates/index.html file. The existence of static/ must be made known in dashboard/settings.py.

# Requirments
## Python Libraries
* pywapi
* django
* requests
* parse

# Applications
## Events
The events app provides the MIT events schedule for the day requested. The MIT RSS feed is parsed and is available at /events. The parsed feed is returned as an array of JSON objects. Each JSON object has a title, description, and time. 

## Nextbus
For information on the Nextbus api visit http://www.nextbus.com/xmlFeedDocs/NextBusXMLFeed.pdf. The Nextbus code evolved from the code used for Dormbase. 

The next shuttles can be accessed from /nextbus. It will return a json object with an array of objects, each of which contains a time_till arrival and a bus name.

## News
The news app provides news from BBC. The feed is parsed and returns an array of JSON objects. Each JSON object has a title and summary. The news can be accessed from /news.

## Weather
Condition codes: http://developer.yahoo.com/weather/#codes

The weather app using the pywapi library and uses Yahoo as its data source. The app can be accessed from /weather and returns a JSON object with current, today, and tomorrow attributes. 'current' has current temp, description, and code. 'today' and 'tomorrow' have high, low, description, code. Units are degrees Fahrenheit. 

# Adding Applications
* Run: python manage.py startapp <appname>
* In the app's directory mkdir static/
* Modify settings.py to search the new static directory
* Add the widget to dashboard/templates/index.html, document the widget with comments
* Add script to index.html

#License and Warranty

Copyright 2013 Simmons Hall

Licensed under LGPL3 (the "License"). You may not use this work except in compliance with the License. You may obtain a copy of the License at http://opensource.org/licenses/lgpl-3.0.html.

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
