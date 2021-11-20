from flask import request
from flask_restful import Resource
from flask_restful import reqparse

import config


class Alert(Resource):
    def post(self):
        if request.headers.get("authorization", "") != config.token:
            return {'error': 'Authorization failed'}, 401
        
