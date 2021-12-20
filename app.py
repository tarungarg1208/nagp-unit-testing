"""Provides ability to invoke APIs"""
import time
from flask import Flask, g, request, Response
from flask_restx import Api

from flasgger import Swagger
from routes.routes import NS_TRADER
from routes.status import NS_STATUS
import logging
LOGGER=logging.getLogger()

APP = Flask(__name__)
Swagger(APP)


VERSION_PREFIX = "v1"
API = Api(
    APP, version=1,
    prefix=f"/{VERSION_PREFIX}",
    title="eBroker",
    description="eBroker - Trader's One Stop Solution"
)
API.add_namespace(NS_STATUS)
API.add_namespace(NS_TRADER)


if __name__ == "__main__":
    APP.run(host="0.0.0.0", port="5000", debug=True)
