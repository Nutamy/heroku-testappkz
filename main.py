# To start APP print in terminal: uvicorn main:app 
# 42 минута видео 
# ссылка: 
# https://us02web.zoom.us/rec/play/aFJARXD3QPoCtyOBtO3JJrToKCdfhTCqQjeFHsKXv9u9q19c11yuyIECqEPPg7uSB1YJuYjZa7qOyhnV.ZuYRBPDhPajuQXvq?continueMode=true&_x_zm_rtaid=__w6UuLjR0W9OtXYi6i5CQ.1611994976641.a37456740e2448d3a05bb05a38643505&_x_zm_rhtaid=946
# api.openweathermap.org/data/2.5/weather?q={almaty}&appid={8b682e300f8818e7cc6238b05b3fc814} 


from typing import Optional
from fastapi import FastAPI, Request
import requests
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory='templates')

db_data = {
    'maria': {
        'age': 22,
        'alumni': 'KIMEP',
        'status': 'bachelor'
    },
    'ali': {
        'age': 25,
        'alumni': 'AUES',
        'status': 'student'
    }
}
class RequestAPI:
    url = 'https://api.quotable.io/random'
    def get_all(self):
        result = requests.get(self.url).json()
        return result
    
    def get_quote(self):
        result = requests.get(self.url).json()

        return result['content']
    
    def get_text(self, name):
        return '%s, hi! I want to say you: %s' % (name, self.get_quote())
class RequestWeather:
    url = 'https://api.oceandrivers.com/v1.0/getWeatherDisplay/London/?period=latestdata'

@app.get('/')
def index(request: Request):
    my_request = RequestAPI()
    advise = my_request.get_quote()
    return templates.TemplateResponse('index.html', {
        'request': request,
        'name': 'Alina',
        'advise': advise})

@app.get("/names")
def names_one(name):
    my_request = RequestAPI()
    return my_request.get_quote()

@app.get("/names/{name}")
def names_one(name):
    my_request = RequestAPI()
    name = name.capitalize()
    return my_request.get_text(name), '\n', my_request.get_all()