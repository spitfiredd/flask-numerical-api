import json

from flask import Blueprint, request

from flask_restplus import Resource, Api
from flask_praetorian import auth_required
from .markov import MarkovChain

API_VERSION_V1 = 1
API_VERSION = API_VERSION_V1

api_bp = Blueprint('api', __name__)
api_v1 = Api(api_bp)


@api_v1.route('/markovchain')
class MarkovWather(Resource):
    method_decorators = [auth_required]

    def get(self):
        data = request.form

        weather_chain = MarkovChain(
            transition_matrix=json.loads(data['transition_matrix']),
            states=json.loads(data['states'])
        )
        states = weather_chain.generate_states(
            current_state=data['current_state'],
            no=int(data['num_obs'])
        )
        return {'states': states}
