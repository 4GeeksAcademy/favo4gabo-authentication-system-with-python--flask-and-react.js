"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_cors import CORS
from flask_jwt_extended import create_access_token

api = Blueprint('api', __name__)

# Allow CORS requests to this API
CORS(api)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200



@api.route('/signup', methods=['POST'])
def register_user():

    body = request.json
    name = body.get("name")
    user_email = body.get("email")
    user_password = body.get("password")

    if name is None or user_email is None or user_password is None:
        return jsonify({"msg": "missing data"}), 400
    # crear un usuario -> crear una instancia de la clase User
    new_user = User(name=name, email=user_email, password=user_password)

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"msg": "user creado satisfactoriamente"})
    except Exception as error:
        db.session.rollback()
        return jsonify({"msg": f"{error}"})
    
@api.route("/login", methods=["POST"])
def login(): 
    body = request.json
    user_email = body.get("email")
    user_password = body.get("password")
    user_query = User.query.filter_by(email=user_email, password=user_password).first()
    if not user_query: 
        return jsonify({"msg": "usuario o contrasena incorrecta"}), 400
    acces_token = create_access_token(identity = user_query.email)
    response_body = {
        "msg": "bienvenido", 
        "acces_token": acces_token, 
        "name": user_query.name
        }
    return jsonify(response_body), 200
    
    
