from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from dotenv import load_dotenv
from datetime import datetime, timedelta
import os

load_dotenv()

def fetch_weather_info_from_llm(destination_city, travel_from_date_str, travel_to_date_str):
    
    llm=ChatGroq(model="mixtral-8x7b-32768", temperature=0)

    prompt_template = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a helpful assistant"),
            ("human", f"""Please suggest how is the weather for city {destination_city} normally for dates {travel_from_date_str} and {travel_to_date_str} in not more than 3 sentences.
                        Please mention expected minimum and maximum temperature and if there could be any chances of rain or snow, based on historical information available to you""")
        ]
    )

    chain = prompt_template | llm | StrOutputParser()
    result = chain.invoke({"destination_city": destination_city, "travel_from_date_str":travel_from_date_str, "travel_to_date_str":travel_to_date_str})
    #print('fetch_weather_info_from_llm result: ', fetch_weather_info_from_llm)
    return result

def fetch_hotel_names_from_llm(destination_city):
    
    llm=ChatGroq(model="mixtral-8x7b-32768", temperature=0)

    prompt_template = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a helpful assistant who can provide best hotels information for a city"),
            ("human", """Please list 6 to 8 good hotels present in {destination_city}. 
            Provide only hotel names and their star rating, i.e. if hotel is a 2-star, 3-star, 4-star etc. 
            List of hotel names should be combination of 3-star, 4-star and 5-star hotels.
            Do not provide any initial text like 'Sure, here are some popular hotels' """)
        ]
    )

    chain = prompt_template | llm | StrOutputParser()
    result = chain.invoke({"destination_city": destination_city})
    return(result)
