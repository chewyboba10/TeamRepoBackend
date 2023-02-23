from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource 
from datetime import datetime
from model.scores import Score

pong_bp = Blueprint("pong_bp", __name__, url_prefix='/api/pong')
pongs_api = Api(pong_bp)

class PongAPI:
    class PongCreate(Resource):    
        def post(self):
            data = request.get_json()

            username = data.get('username')
            if username is None or len(username) != 3:
                return {'message': f'username is missing or longer than 3 characters'}, 210
                
            # Change later to exclude negative scores
            score = data.get('score')
            if score is None or len(score) <= 0:
                return {'message': f'Score does not exist, is missing, or is invalid'}, 210 
                    
            dos = data.get('dos')

            sob = Score(username=username, score=score)

            if dos is not None:
                try:
                    sob.dos = datetime.strptime(dos, '%m-%d-%Y').date()
                except:
                    return {'message': f'Date obtained score format error {dos}, must be mm-dd-yyyy'}, 210
            
            user = sob.create()
            if user:
                return jsonify(user.make_dict())
            return {'message': f'Processed {username}, either a format error or Username {username} is duplicate'}, 210

    class ScoreListAPI(Resource):
        def get(self):
            scores = Score.query.all()
            json_ready = [user.make_dict() for user in scores]
            return jsonify(json_ready)

    scores_api.add_resource(ScoreCreate, '/addScore')
    scores_api.add_resource(ScoreListAPI, '/scoresList')


