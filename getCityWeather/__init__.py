import logging
import azure.functions as func
import requests 
from app.generateID import GenerateID
import datetime as dt
import time

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = 'd85eaab2aca141c7138eff86c67a98a7'

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('The function processed a request.')


    """ user_test = GenerateID(name)
    user_test = user_test.associate_city(city) """
  
    req_body = req.get_json()
    
    city = req_body.get('city')
    name = req_body.get('name')

    url = f"{BASE_URL}appid={API_KEY}&q={city}"

    if city:
        response = requests.get(url).json()
        return func.HttpResponse(f"Hello {name},this function executed successfully. We are collecting the data about {city} \n Here is the information: {response}")   
    else:
        return func.HttpResponse(
             "This function executed successfully. Pass a city in the query string or in the request body for info about yout city.",
             status_code=200
        ) 

""" 
http://localhost:7071/api/getCityWeather?name=Pedro 
                                             ^ 
                                             Req params 
"""