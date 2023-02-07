from model.gameHistories import History
from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource 
from datetime import datetime
import datetime

history_bp = Blueprint("history_api", __name__, url_prefix='/api/history')
history_API = Api(history_bp)

class HistoryAPI_Create(Resource):
    def post(self):
        data = request.get_json()

        username = data.get('username')
        if username is None or len(username) != 3:
            return {'message': f'Username is missing, or is not 3 characters'}, 210
        
        # Change later to exclude negative scores
        score = data.get('score')
        if score is None:
            return {'message': f'Score does not exist or is missing'}, 210 
            
        dos = data.get('dos')

        tos = data.get('tos')

        userPerson = History(username=username)

        if dos is not None:
            try:
                userPerson.dos = datetime.strptime(dos, '%m-%d-%Y').date()
            except:
                return {'message': f'Date obtained score format error {dos}, must be mm-dd-yyyy'}, 210
        
        if tos is not None:
            try:
                userPerson.tos = tos #Change later to str(tos) is it doesn't work
            except:
                return {'message': f'Time has a format error {tos}, must be hh:mm:ss'}, 210
            
        user = userPerson.create()

        if user:
            return jsonify(user.make_dict())
        return {'message': f'Processed {username}, either username is a format error or {username} is duplicate'}, 210

class HistoryListAPI(Resource):
    def get(self):
        histories = History.query.all()
        json_ready = [user.make_dict() for user in histories]
        return jsonify(json_ready)

history_API.add_resource(HistoryAPI_Create, '/createGameHistory')
history_API.add_resource(HistoryListAPI, '/gameHistoriesList')
