from django.http import HttpResponse
import pywapi
import json

def getWeather(request):
    # Yahoo WOEID
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
    
    weather = { 'current': current,
                'today': today,
                'tomorrow': tomorrow,}
    
    jsonout = json.dumps(weather)
    return HttpResponse(jsonout, mimetype="application/json")

def code2image(code):
    return "img"
