from flask import Flask
import database.database
import services.customer_ord_line as customer_ord_line
import services.customer_orders as customer_order
import services.weather as weather
from flask import make_response

app = Flask(__name__)

import json
# import requests

app = Flask(__name__)
# from database import config


@app.route(
    '/order_status',
    methods=['GET']
)
def order_status():
    result = customer_ord_line.get_customer_ord_lines()
    return make_response(result, 200)

@app.route(
    '/season',
    methods=['GET']
)
# NOTA en el ejemplo  que se muestra en el documento para la salida de los ID 
# 112-5230502-8173028 y 112-5230502-8173028
# la salida que se muestra en el ejemplo es incorrecta
# la salida correcta segun sus fechas deberia de ser FALL Y WINTER respectivamente

def season():
    result = customer_order.get_season()
    return make_response(result, 200)
    pass


@app.route(
    '/weather_change',
    methods=['GET']
)


def detecting_change():
    result = weather.detect_weather_change()
    return make_response(result, 200)
    pass