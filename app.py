from flask import Flask
import database.database

app = Flask(__name__)

import json
# import requests

app = Flask(__name__)
# from database import config


@app.route(
    '/order_status',
    methods=['GET']
)
def order_status(request):
    pass