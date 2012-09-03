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
                    'code': tmp_condition['code'], }

        tmp_today = forecast['forecasts'][0]
        today = { 'high': tmp_today['high'],
                  'low': tmp_today['low'],
                  'description': tmp_today['text'],
                  'code': tmp_today['code']}

        tmp_tomorrow = forecast['forecasts'][1]
        tomorrow = { 'high': tmp_tomorrow['high'],
                     'low': tmp_tomorrow['low'],
                     'description': tmp_tomorrow['text'],
                     'code': tmp_tomorrow['code']}

    except:
        current = {'temp': 'NA',
                   'description': 'NA',
                   'code': 'NA',}

        today = tomorrow = {'high': 'NA',
                            'low': 'NA',
                            'description': 'NA',
                            'code': 'NA',}
    
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
	return weather[ code ]
