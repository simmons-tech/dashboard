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
import pywapi
import json

def getWeather(request):
    try:
        # Zip Code
        location_id = '02139'
        forecast = pywapi.get_weather_from_yahoo(location_id, '')

        tmp_condition = forecast['condition']
        current = { 'temp': tmp_condition['temp'],
                    'description': tmp_condition['text'],
                    'icon': code2image(tmp_condition['code']),}

        tmp_today = forecast['forecasts'][0]
        today = { 'high': tmp_today['high'],
                  'low': tmp_today['low'],
                  'description': tmp_today['text'],
                  'icon': code2image(tmp_today['code']),}

        tmp_tomorrow = forecast['forecasts'][1]
        tomorrow = { 'high': tmp_tomorrow['high'],
                     'low': tmp_tomorrow['low'],
                     'description': tmp_tomorrow['text'],
                     'icon': code2image(tmp_tomorrow['code']),}

    except:
        current = {'temp': 'NA',
                   'description': 'NA',
                   'icon': 'NA',}

        today = tomorrow = {'high': 'NA',
                            'low': 'NA',
                            'description': 'NA',
                            'icon': 'NA',}
    
    weather = { 'title': 'Yahoo! Weather',
                'current': current,
                'today': today,
                'tomorrow': tomorrow,}
    
    jsonout = json.dumps(weather)
    return HttpResponse(jsonout, mimetype="application/json")

def code2image(code):
    weather = {
		'0':'windy.png',
		'1':'windy.png',
		'2':'windy.png',
		'3':'thunder.png',
		'4':'thunder.png',
		'5':'mixed.png',
		'6':'mixed.png',
		'7':'mixed.png',
		'8':'mixed.png',
		'9':'rain.png',
		'10':'mixed.png',
		'11':'rain.png',
		'12':'rain.png',
		'13':'snow.png',
		'14':'snow.png',
		'15':'snow.png',
		'16':'snow.png',
		'17':'mixed.png',
		'18':'mixed.png',
		'19':'foggy.png',
		'20':'foggy.png',
		'21':'foggy.png',
		'22':'foggy.png',
		'23':'windy.png',
		'24':'windy.png',
		'25':'cold.png',
		'26':'cloudy.png',
		'27':'cloudy.png',
		'28':'cloudy.png',
		'29':'patchy_night.png',
		'30':'patchy.png',
		'31':'clear_night.png',
		'32':'sunny.png',
		'33':'clear_night.png',
		'34':'sunny.png',
		'35':'mixed.png',
		'36':'hot.png',
		'37':'thunder.png',
		'38':'thunder.png',
		'39':'thunder.png',
		'40':'rain.png',
		'41':'snow.png',
		'42':'snow.png',
		'43':'snow.png',
		'44':'patchy.png',
		'45':'thunder.png',
		'46':'snow.png',
		'47':'thunder.png',
		'3200':'no_icon.png'
	}

    # path that browser will use to find weather images
    image_path = "/static/img/"
    
    return "{}{}".format(image_path, weather[ code ])
