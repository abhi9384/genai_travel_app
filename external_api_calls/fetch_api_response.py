import requests
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from dotenv import load_dotenv
from datetime import datetime, timedelta
import os
import math

# API call to fetch weather information
def fetch_weather_info_from_api(destination_city, travel_from_date_str, travel_to_date_str):
    
    travel_from_date = datetime.strptime(travel_from_date_str, '%Y-%m-%d').date()
    travel_to_date = datetime.strptime(travel_to_date_str, '%Y-%m-%d').date()
    travel_date = travel_from_date

    while travel_date <= travel_to_date:
        try: 
            #print("travel_date variable: ", travel_date)
            weather_api_key = os.getenv("WEATHER_API_KEY")
            #url = f"http://api.weatherapi.com/v1/forecast.json?key="+weather_api_key+"&q=" + destination_city&days=5"
            url = f"http://api.weatherapi.com/v1/future.json?key="+weather_api_key+"&q=" + destination_city + "&dt=" + str(travel_date)
            #print("url: ", url)
            response = requests.get(url=url)
            response_json = response.json()
            #print(response_json)
            
            if 'forecast' in response_json:
                forecast_days = response_json["forecast"]["forecastday"]
                #print('forecast: ', forecast_days)

                for count, element in enumerate(forecast_days):
                    #print('Day ', count+1, ' Date: ', element["date"])
                    #print('weather: ', element["day"]["condition"]["text"], ' average temperature: ', element["day"]["avgtemp_c"],
                    #    ' weather icon: ', element["day"]["condition"]["icon"])
                    text = 'Day ', count+1, ' Date: ', element["date"], 'weather: ', element["day"]["condition"]["text"], ' average temperature: ', element["day"]["avgtemp_c"]
                    api_response += text
                    #print('Day ', count+1, ' api_response: ', api_response)
            else:
                api_response = "forecast tag not present in response_json"
                #print("else block: api_response: ", api_response)
        except Exception as e:
            print("An error occurred: ", repr(e))
            api_response = "Weather information cannot be retrieved for now"
            #print("finally block: api_response: ", api_response)
        finally:
            travel_date += timedelta(days=1)    
    return api_response

# API call to fetch airfares
