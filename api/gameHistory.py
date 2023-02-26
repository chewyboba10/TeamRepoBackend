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

        userPerson = History(username=username,
                             score=score)

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

class HistoryUpdate(Resource):
    def put(self):
        data = request.get_json()

        username = data.get('username')
        if username is None or len(username) != 3:
            return {'message': f'Username is missing, or is not 3 characters'}, 210
        
        # Change later to exclude negative scores
        score = data.get('score')
        if score is None:
            return {'message': f'Score does not exist or is missing'}, 210 
        
        userPerson = History(username=username,
                             score=score)

        user = userPerson.update()

        if user:
            return jsonify(user.make_dict())
        return {'message': f'Processed {username}, either username is a format error or {username} is duplicate'}, 210

class HistoryDelete(Resource):
    def delete(self, username):
        historyDeleting = History.query.get(username)
        if historyDeleting:
            historyDeleting.delete()
            return {'message': f'Username {username} profile deleted'}, 210
        else:
            return {'message': f'Username {username} profile not found'}, 210
        
history_API.add_resource(HistoryAPI_Create, '/createGameHistory')
history_API.add_resource(HistoryListAPI, '/gameHistoriesList')
history_API.add_resource(HistoryUpdate, '/historyUpdate')
history_API.add_resource(HistoryDelete, '/delete/<string:username>')
