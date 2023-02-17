from flask import Flask

app = Flask(__name__)

import json
# import requests

app = Chalice(app_name='ezaudita')
# from database import config


@app.route(
    '/order_status',
    methods=['GET', 'POST', 'PUT', 'DELETE']
)
