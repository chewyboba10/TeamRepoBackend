from ..model.scores import Score
from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource 
from datetime import datetime

scores_bp = Blueprint("score", __name__)
scores_api = Api(scores_bp)

class ScoreAPI(Resource):
    def get(self):
        data = request.get_json()

        name = data.get('name')
        if name is None or len(name) < 2:
            return {'message': f'Name is missing, or is less than 2 characters'}, 210

        uid = data.get('uid')
        if uid is None or len(uid) < 2:
            return {'message': f'User ID is missing, or is less than 2 characters'}, 210
        
        score = data.get('score')
        if score is None:
            return {'message': f'Score does not exist or is missing'}, 210 
        
        dos = data.get('dos')

        sob = Score(name=name, 
                    uid=uid)

        if dos is not None:
            try:
                sob.dos = datetime.strptime(dos, '%m-%d-%Y').date()
            except:
                return {'message': f'Date obtained score format error {dos}, must be mm-dd-yyyy'}, 210

class ScoreListAPI(Resource):
    def get(self):
        scores = Score.query.all()
        json_ready = [user.read() for user in scores]
        return jsonify(json_ready)

scores_api.add_resource(ScoreAPI, '/scores')
scores_api.add_resource(ScoreListAPI, '/scoresList')
