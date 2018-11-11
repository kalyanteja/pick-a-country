from datetime import datetime
import os
import pytz
import requests
import math
API_URL = ('https://restcountries.eu/rest/v2/alpha/{}')
APP_ALL_URL = 'https://restcountries.eu/rest/v2/all'
def query_api(alpha):
    try:
        print(API_URL.format(alpha))
        data = requests.get(API_URL.format(alpha)).json()
    except Exception as exc:
        print(exc)
        data = None
    return data
	
def query_api_all():
    try:
        print(APP_ALL_URL)
        data = requests.get(APP_ALL_URL).json()
    except Exception as exc:
        print(exc)
        data = None
    return data