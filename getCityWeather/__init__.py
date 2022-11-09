import logging
import azure.functions as func
import requests 
from app.generateID import GenerateID
""" import datetime as dt
import time  """

""" BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = open('D:\DayForecast\getCityWeather\api_key','r').read() """

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('The function processed a request.')

    city =  req.params.get('city')
    name =  req.params.get('name')
    
    user_test = GenerateID(name)
    user_test = user_test.associate_city(city)

    """ url = BASE_URL + 'appid=' + API_KEY + '&q=' + city """

    if not city:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            city = req_body.get('city')

    if city:
        return func.HttpResponse(f"Hello {name},this function executed successfully. We are collecting the data about {city}")   
    else:
        return func.HttpResponse(
             "This function executed successfully. Pass a city in the query string or in the request body for info about yout city.",
             status_code=200
        ) 


    """ response = requests.get(url).json()

    print(response) """