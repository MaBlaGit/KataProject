#! /usr/bin/python

import bottle
from bottle import route, error
import weather_api_script


@route('/index', method='GET')
def index():
    city = bottle.request.GET.get("my_city")
    if city is None or city == "":
        return bottle.template('index_page')
    return bottle.redirect('/index/%s' % city)


@route('/index/<city_name>')
def weather_page(city_name):
    weather_api = weather_api_script.get_current_weather(city_name)
    if isinstance(weather_api, list):
        my_weather_many_cities = list()
        for city in weather_api:
            my_weather_many_cities.append(city[0])
        return bottle.template(
                            'current_weather_more_cities',
                             many_cities=my_weather_many_cities,
        )
    else:
        my_weather = [weather_api[0], weather_api[1], weather_api[2], weather_api[3], weather_api[4], weather_api[5],
                      weather_api[6],  weather_api[7],  weather_api[8]]
        return bottle.template(
                            'current_weather',
                            google_map_api_key=weather_api[0],
                            city_name=weather_api[1],
                            latitude=weather_api[2],
                            longitude=my_weather[3],
                            weather_max_temp=my_weather[4],
                            weather_min_temp=my_weather[5],
                            weather_wind=my_weather[6],
                            humidity=my_weather[7],
                            country_iso_code=weather_api[8],
        )


@route('/index/selected')
def selected_city():
    city_name = "Warsaw"
    city_id = bottle.request.GET.get("id")
    x = weather_api_script.get_current_weather_by_id(city_name, city_id)
    # print x[0]
    return bottle.template('selected_city_from_cities', city_data=x)


@error(404)
@error(500)
def error500(error):
    return bottle.template('error_page')

if __name__ == '__main__':
    bottle.run(host='localhost', port=8080)
