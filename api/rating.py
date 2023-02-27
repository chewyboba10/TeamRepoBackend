from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource 
from model.ratings import rating

rating_bp = Blueprint("rating_api", __name__, url_prefix='/api/rating')
rating_API = Api(rating_bp)

class RatingAPI_Create(Resource):
    def post(self):
        data = request.get_json()

        username = data.get('username')
        if username is None or len(username) != 3:
            return {'message': f'Username is missing, or is not 3 characters'}, 210
        
        rating = data.get('rating')
        if score is None:
            return {'message': f'Rating does not exist or is missing'}, 210 

        userPerson = Rating(username=username, rating=score)

        user = userPerson.create()

        if user:
            return jsonify(user.make_dict())
        return {'message': f'Processed {username}, either username is a format error or {username} is duplicate'}, 210

class RatingListAPI(Resource):
    def get(self):
        ratings = ratings.query.all()
        json_ready = [user.make_dict() for user in ratings]
        return jsonify(json_ready)

class RatingsUpdate(Resource):
    def put(self):
        data = request.get_json()
        usernameData = data.get('username')
        ratingsData = data.get('rating')
        userUpdate = Ratings.query.filter_by(_username = usernameData).first() 
        if userUpdate:
            userUpdate.update(rating = ratingData)
            return jsonify(userUpdate.make_dict())
        else:
            return {'message': f'{usernameData} not found'}, 210

class RatingDelete(Resource):
    def delete(self):
        data = request.get_json()
        getID = data.get('id')
        ratingDeleting = Rating.query.get(getID)
        if ratingDeleting:
            ratingDeleting.delete()
            return {'message': f'Username {getID} profile deleted'}, 210
        else:
            return {'message': f'Username {getID} profile not found'}, 210
        
rating_API.add_resource(RatingAPI_Create, '/createRating')
rating_API.add_resource(RatingListAPI, '/RatingList')
rating_API.add_resource(RatingUpdate, '/RatingUpdate')
rating_API.add_resource(RatingDelete, '/deleteRating')
