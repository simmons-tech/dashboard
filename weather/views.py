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

# def code2image(code):
#     weather = { '0': 'no_icon.png',
#                 '1': 'no_icon.png'
#                 '2': 'no_icon.png',
#                 '3': 'severe_thunderstorms.png',
#                 '4': 'thunderstorms.png',
#                 '5': 'mixed_rain_and_snow.png',
#                 '6': 'mixed_rain_and_snow.png',
#                 '7': 'mixed_rain_and_snow.png',
#                 '8': 'freezing.png',
#                 '9': 'drizzle.png',
#                 '10': 'freezing.png',
#                 '11': 'showers.png',
#                 '12': 'showers.png',
#                 '13': 'snow.png',
#                 '14': 'mixed_rain_and_snow.png',
#                 '15': 'blowing_snow.png',
#                 '16': 'snow.png',
#                 '17': 'hail.png',
#                 '18': 'hail.png',
#                 '19': 'dust.png',
#                 '20': 'foggy.png',
#                 '21': 'no_icon.png',
#                 '22': 'smoky.png',
#                 '23': 'no_icon.png',
#                 '24': 'windy.png',
#                 '25': 'no_icon.png',
#                 '26': 'cloudy.png',
#                 '27': 'mostly_cloudy_night.png',
#                 '28': 'mostly_cloudy_day.png',
#                 '29': 'partly_cloudy_night.png',
#                 '30': 'partly_cloudy_day.png',
#                 '31': 'clear_night.png',
#                 '32': 'sunny.png',
#                 '33': 'fair', (night)
#                 '34': 'fair', (day)
#                 '35': 'mixed', rain and hail
#                 '36': 'hot.png',
#                 '37': 'thunderstorms.png',
#                 '38': 'thunderstorms.png',
#                 '39': 'thunderstorms.png',
#                 '40': 'scattered', showers
#                 '41': 'heavy', snow
#                 '42': 'scattered', snow showers
#                 '43': 'heavy', snow
#                 '44': 'partly', cloudy
#                 '45': 'thundershowers',
#                 '46': 'snow', showers
#                 '47': 'isolated', thundershowers
#                 '3200': 'not', available }
