# https://www.weatherapi.com/api-explorer.aspx#forecast

#Note: http://api.weatherapi.com/v1/future.json - works only for Date between 14 days and 300 days from today in the future in yyyy-MM-dd format
# for earlier dates use forecast.json

from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from external_api_calls.fetch_api_response import fetch_weather_info_from_api
from llm_calls.fetch_llm_response import fetch_weather_info_from_llm, fetch_hotel_names_from_llm
import requests
from dotenv import load_dotenv
from datetime import datetime, timedelta
import os

load_dotenv()

print("*************** Welcome ***************")
destination_city = 'Singapore' #input("Where do you want to go?: ")
travel_from_date_str = '2024-12-15' #input("Please enter your journey start date in YYYY-MM-DD format: ")
travel_to_date_str = '2024-12-17' #input("Please enter your journey end date in YYYY-MM-DD format: ")
response_from_api = fetch_weather_info_from_api(destination_city, travel_from_date_str, travel_to_date_str)
#print('response_from_api: ', response_from_api)

if response_from_api == "forecast tag not present in response_json":
    response_from_llm = fetch_weather_info_from_llm(destination_city, travel_from_date_str, travel_to_date_str)
    print('Weather Information: ', response_from_llm)

#Get Hotels
hotel_names = fetch_hotel_names_from_llm(destination_city)
print('Some popular hotel names of ', destination_city)
print(hotel_names)
