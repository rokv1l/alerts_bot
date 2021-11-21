from datetime import date, datetime

from flask import request
from flask_restful import Resource
from flask_restful import reqparse

import config
from src.utils import get_logger
from src.database import session_maker, Alert

logger = get_logger(__name__, config.logs_path)


class Alert(Resource):
    def post(self):
        if request.headers.get("authorization", "") != config.token:
            return {'error': 'Authorization failed'}, 401
        parser = reqparse.RequestParser()
        parser.add_argument('message', type=str, reqired=True)
        args = parser.parse_args()
        logger.info(f'{request.remote_addr}: Alert.post: params={args}')
        with session_maker() as session:
            alert = Alert(
                message=args.get('message'),
                datetime=datetime.now()
            )
            session.add(alert)
            session.commit()
