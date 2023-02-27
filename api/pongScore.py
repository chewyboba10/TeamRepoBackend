from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource 
from datetime import datetime
from model.pongScores import Pong

pong_bp = Blueprint("pong_bp", __name__, url_prefix='/api/pong')
pongs_api = Api(pong_bp)

class PongAPI:
    class PongCreate(Resource):    
        def post(self):
            data = request.get_json()

            user1 = data.get('user1')
            if user1 is None or len(user1) != 3:
                return {'message': f'username 1 is missing or longer than 3 characters'}, 210
                
            user2 = data.get('user2')
            if user2 is None or len(user2) != 3:
                return {'message': f'username 2 is missing or longer than 3 characters'}, 210
            
            # Change later to exclude negative scores
            score1 = data.get('score1')
            if score1 is None or len(score1) <= 0:
                return {'message': f'Score 1 does not exist, is missing, or is invalid'}, 210 

            score2 = data.get('score2')
            if score2 is None or len(score2) <= 0:
                return {'message': f'Score 2 does not exist, is missing, or is invalid'}, 210 
                
            result1 = data.get('result1')
            if result1 is None:
                return {'message': f'Game result does not exist or is missing'}, 210 
            
            result2 = data.get('result2')
            if result2 is None:
                return {'message': f'Game result does not exist or is missing'}, 210 
            
            scoreDate = data.get('scoreDate')

            pongProfile = Pong(user1=user1, user2=user2, score1=score1, score2=score2, result1=result1, result2=result2)

            if scoreDate is not None:
                try:
                    pongProfile.scoreDate = datetime.strptime(scoreDate, '%m-%d-%Y').date()
                except:
                    return {'message': f'Date obtained score format error {scoreDate}, must be mm-dd-yyyy'}, 210
            
            user = pongProfile.create()
            if user:
                return jsonify(user.make_dict())
            return {'message': f'Processed {user1} and/or {user2}, either a format error or Usernames {user1} and/or {user2} is duplicate'}, 210

    class PongListAPI(Resource):
        def get(self):
            pongScores = Pong.query.all()
            json_ready = [user.make_dict() for user in pongScores]
            return jsonify(json_ready)

    pongs_api.add_resource(PongCreate, '/addPongScore')
    pongs_api.add_resource(PongListAPI, '/pongList')


