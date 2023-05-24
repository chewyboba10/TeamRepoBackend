from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource 
from datetime import datetime
from model.geoguesser-model import Geoguesser

# Create score blueprint for API
scores_bp = Blueprint("scores_bp", __name__, url_prefix='/api/score')
# Score API derived from blueprint
scores_api = Api(scores_bp)

# Define class for the API
class ScoreAPI:
    # Define class to create a user using the POST method
    class ScoreCreate(Resource):    
        # def post(self) creates POST method
        def post(self):
            # Gets the data from postman or frontend
            data = request.get_json()

            # Gets the username, checks if the username is exactly 3 characters. If it isn't 3 characters, POST is terminated
            username = data.get('username')
            if username is None or len(username) != 3:
                return {'message': f'username is not 3 characters'}, 210
                
            # Gets the score, checks if the score has more than 0 digits. If there is no digits, POST is terminated
            score = data.get('score')
            if score is None or len(score) <= 0:
                return {'message': f'Score does not exist, is missing, or is unrealistic'}, 210 
            
            # Gets the date of score
            dos = data.get('dos')
            
            # sob uses class Score to create a user
            sob = Score(username=username, score=score)

            # Checks if date of score exists, reformats it to mm-dd-yyyy
            if dos is not None:
                try:
                    sob.dos = datetime.strptime(dos, '%m-%d-%Y').date()
                except:
                    return {'message': f'Date obtained has a format error {dos}, must be mm-dd-yyyy'}, 210
            
            # CREATE operation: creates user
            user = sob.create()
            if user:
                # make_dict() function to return a dictionary for the user
                return jsonify(user.make_dict())
            # returns error message if unable to return a dictionary
            return {'message': f'Processed {username}, there is likely a format error'}, 210

    # GET method displays the data from the API
    class ScoreListAPI(Resource):
        # def get(self) does the GET method
        def get(self):
            # Gets all the data from Score and returns a dictionary
            scores = Score.query.all()
            json_ready = [user.make_dict() for user in scores]
            return jsonify(json_ready)

    # PUT method updates data in the API
    class ScoreUpdate(Resource):
        # def put(self) does the PUT method
        def put(self):
            # Gets the data from postman or frontend
            data = request.get_json()

            # Gets the username
            usernameData = data.get('username')

            # Gets the score, score is going to be updated
            scoreData = data.get('score')

            # Gets the user through the username
            userUpdating = Score.query.filter_by(_username = usernameData).first()
            if userUpdating:
                # Updates the score for the user
                userUpdating.update(score = scoreData)
                # Returns a dictionary to confirm that the score was updated
                return jsonify(userUpdating.make_dict())
            else:
                # Error message if update fails
                return {'message': f'{usernameData} not found'}, 210

    # Delete method deletes data in the API
    class ScoreDelete(Resource):
        # def delete(self) does the DELETE method
        def delete(self):
            # Gets the data from postman or frontend
            data = request.get_json()

            # Gets the ID
            getID = data.get('id')

            # Gets the user through the ID
            historyDeleting = Score.query.get(getID)
            if historyDeleting:
                # Deletes the user according to its ID number
                historyDeleting.delete()
                return {'message': f'Profile #{getID} deleted'}, 210
            else:
                # Error message if delete fails
                return {'message': f'Profile #{getID} not found'}, 210
    
    # Endpoints, uses URL prefix and '/' to refer to different classes which corresponds to different methods
    scores_api.add_resource(ScoreCreate, '/addScore')
    scores_api.add_resource(ScoreListAPI, '/scoresList')
    scores_api.add_resource(ScoreUpdate, '/updateScore')
    scores_api.add_resource(ScoreDelete, '/deleteScore')

