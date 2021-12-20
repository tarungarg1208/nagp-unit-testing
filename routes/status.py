"""Module for status health check API."""
from datetime import datetime
from os import path
# from flask_restplus import Namespace, Resource
from flask_restx import Namespace, Resource

NS_STATUS = Namespace("status", description="Status/Healthcheck related routes")

@NS_STATUS.route("")
class Status(Resource):
    """Status class to check health of App"""

    @NS_STATUS.doc("get_status")
    @staticmethod
    def get():
        """Returns health check API response"""
        return dict(status="healthy", time=str(datetime.now()), version='v1')
