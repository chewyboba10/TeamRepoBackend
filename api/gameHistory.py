from model.scores import Score
from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource 
from datetime import datetime

scores_bp = Blueprint("score", __name__, url_prefix='/api/score')
scores_api = Api(scores_bp)

class HistoryAPI(Resource):
    def get(self):
        data = request.get_json()

        name = data.get('name')
        if name is None or len(name) < 2:
            return {'message': f'Name is missing, or is less than 2 characters'}, 210

        username = data.get('username')
        if username is None or len(username) < 2:
            return {'message': f'User ID is missing, or is less than 2 characters'}, 210
        
        # Change later to exclude negative scores
        score = data.get('score')
        if score is None:
            return {'message': f'Score does not exist or is missing'}, 210 
            
        dos = data.get('dos')

        sob = Score(name=name, 
                    username=username)

        if dos is not None:
            try:
                sob.dos = datetime.strptime(dos, '%m-%d-%Y').date()
            except:
                return {'message': f'Date obtained score format error {dos}, must be mm-dd-yyyy'}, 210
        
        user = sob.create()
        if user:
            return jsonify(user.make_dict())
        return {'message': f'Processed {name}, either a fromat error or User ID {username} is duplicate'}, 210

class ScoreListAPI(Resource):
    def get(self):
        scores = Score.query.all()
        json_ready = [user.make_dict() for user in scores]
        return jsonify(json_ready)

scores_api.add_resource(ScoreAPI, '/scores')
scores_api.add_resource(ScoreListAPI, '/scoresList')
