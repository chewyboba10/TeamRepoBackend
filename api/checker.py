from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource 
from datetime import datetime
from model.checkers import Checkers

checkers_bp = Blueprint("checkers_bp", __name__, url_prefix='/api/checkers')
checkers_api = Api(checkers_bp)

class CheckersAPI:
    class CheckersResultsCreate(Resource):    
        def post(self):
            data = request.get_json()

            uidB = data.get('uidB')
            if uidB is None or len(uidB) != 3 :
                return {'message': f'username for black is missing or longer than 3 characters'}, 210
                
            # Change later to exclude negative scores
            resultB = data.get('resultB')
            if resultB is None or not resultB in ['Win', 'Loss']:
                return {'message': f'Result does not exist, is missing, or is invalid'}, 210
            
            uidR = data.get('uidR')
            if uidR is None or len(uidR) != 3 :
                return {'message': f'username for black is missing or longer than 3 characters'}, 210
                
            # Change later to exclude negative scores
            resultR = data.get('resultR')
            if resultR is None or not resultR in ['Win', 'Loss']:
                return {'message': f'Result does not exist, is missing, or is invalid'}, 210

             
            dos = data.get('dos')

            cob = Checkers(uidB=uidB, resultB=resultB, uidR=uidR, resultR=resultR)

            if dos is not None:
                try:
                    cob.dos = datetime.strptime(dos, '%m-%d-%Y').date()
                except:
                    return {'message': f'Date obtained score format error {dos}, must be mm-dd-yyyy'}, 210
            
            user = cob.create()
            if user:
                return jsonify(user.make_dict())
            return {'message': f'Processed {uidB} or {uidR}, either a format error or Usernames {uidB} or {uidR} is duplicate'}, 210

    class CheckersListAPI(Resource):
        def get(self):
            checkers = Checkers.query.all()
            json_ready = [user.make_dict() for user in checkers]
            return jsonify(json_ready)

    checkers_api.add_resource(CheckersResultsCreate, '/addCheckersGame')
    checkers_api.add_resource(CheckersListAPI, '/checkersList')


