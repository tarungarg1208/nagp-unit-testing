"""
This package contains utility functions
"""
from json import dumps
from webargs.flaskparser import FlaskParser
from flask import jsonify, make_response, abort
import logging

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)

class _Parser(FlaskParser):
    "custom parser to properly format validation errors on request args"
    def handle_error(self, error, req, schema, *, error_status_code, error_headers): # pylint: disable=unused-argument
        "format schema errors for easier consumption"
        LOGGER.warning('INVALID_REQUEST', str(error.messages))
        abort(make_response(jsonify(error.messages), 400))

PARSER = _Parser()
