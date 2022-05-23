"""MODULE"""
import json
import os
import socket
import requests
from flask import Flask, request, jsonify
import response
from JSONExceptionHandler import JSONExceptionHandler
app = Flask(__name__)
USER_URL = None
TOKEN_URL = None
HOST = "0.0.0.0"
PORT = 5001
if os.environ.get('FLASK_ENV') == 'development':
    # app.logger.info(os.environ.get('FLASK_ENV'))
    app.config.from_object('config.Development')
    USER_URL = "http://localhost:5002"
    TOKEN_URL = "http://localhost:5003"
    print("Dev")
elif os.environ.get('FLASK_ENV') == 'testing':
    # app.logger.info(os.environ.get('FLASK_ENV'))
    app.config.from_object('config.Testing')
    USER_URL = "http://localhost:5002"
    TOKEN_URL = "http://localhost:5003"
else:
    # app.logger.info(os.environ.get('FLASK_ENV'))
    app.config.from_object('config.Production')
    USER_URL = "http://user:5002"
    TOKEN_URL = "http://token:5003"
@app.route("/",methods=["GET"])
def home():
    """_summary_

    Returns:
        _type_: _description_
    """
    test=  app.config.get("FLASK_ENV")
    return f'GATEWAY INI ADALAH MODE: {test} SOCKETNAME: {socket.gethostname()}'

@app.route("/initial",methods=["GET"])
def initial():
    """_summary_

    Returns:
        _type_: _description_
    """
    response = requests.get(f"{USER_URL}/create")
    # sent ok response
    return jsonify({
        "message":response.json()['message']
        }), 200


@app.route("/register",methods=["POST"])
def register():
    """_summary_

    Returns:
        _type_: _description_
    """
    payload = json.loads(request.data)
    required_fields = ['first_name', 'last_name',
            'email', 'username', 'password']
    #check required field
    for field in required_fields:
        if field not in payload:
        # abort(400, '%s is required' % field)
            return jsonify({
                "message":f'{field} is required'
                }), 400
    # hit service user
    data_payload = {
        "first_name":payload["first_name"],
        "last_name":payload["last_name"],
        "email":payload["email"],
        "username" : payload["username"],
        "password": payload["password"]
    }
    response = requests.post(f"{USER_URL}/register", json=data_payload)
    # sent error response
    if response.status_code != 200 :
        return jsonify({
            "message":response.json()['message']
        }), 400
    # sent ok response
    return jsonify({
        "message":"success",
        "data": response.json()['data']
    }), 200
@app.route("/login",methods=["POST"])
def login():
    result = dict()
    """_summary_

    Returns:
        _type_: _description_
    """
    payload = json.loads(request.data)
    # hit service user
    data_payload = {
        "username" : payload["username"],
        "password": payload["password"]
    }
    response = None
    try:
        response = requests.post(f"{USER_URL}/login", json=data_payload)
    except requests.exceptions.RequestException as exception:  # This is the correct syntax
        return jsonify({
            "message":f"{exception}"
        }), 400
    #response = requests.post(f"{user_url}/login", json=data_payload)
    response_json = response.json()
    # sent error response
    if response.status_code != 200 :
        return jsonify({
            "message":response_json['message']
        }), 400
    data_payload = {
        "id" : response_json['data']["public_id"]
    }
    try:
        response = requests.post(f"{TOKEN_URL}/generate", json=data_payload)
    except requests.exceptions.RequestException as exception:  # This is the correct syntax
        return jsonify({
            "message":f"{exception}"
        }), 400
    response_json = response.json()
    # sent ok reponse
    return jsonify({
        "message":"success",
        "token":response_json["token"],
        "token_refresh":response_json["token_refresh"]
    }), 200
@app.route("/refresh",methods=["POST"])
def refresh():
    """_summary_

    Returns:
        _type_: _description_
    """
    payload = json.loads(request.data)
    # hit service user
    data_payload = {
        "token" : payload["token"]
    }
    response = None
    try:
        response = requests.post(f"{TOKEN_URL}/refresh", json=data_payload)
    except requests.exceptions.RequestException as exception:  # This is the correct syntax
        return jsonify({
            "message":f"{exception}"
        }), 400
    response_json = response.json()
    # sent error response
    if response.status_code != 200 :
        return jsonify({
            "message":response_json['message']
        }), 401
    # sent ok reponse
    return jsonify({
        "message":"success",
        "token":response_json["token"],
        "token_refresh":response_json["token_refresh"]
    }), 200
@app.route("/loginagri",methods=["POST"])
def loginagri():
    """_summary_

    Returns:
        _type_: _description_
    """
    payload = json.loads(request.data)
    # hit service user
    data_payload = {
        "username" : payload["username"],
        "password": payload["password"]
    }
    response = requests.post(f"{USER_URL}/loginagri", json=data_payload)
    response_json = response.json()
    # sent error response
    if response.status_code != 200 :
        return jsonify({
            "message":"Username is not registered please check",
            "data": {
                "username":payload["username"]
            }
        }), 400
    data_payload = {
        "id" : response_json["username"]
    }
    response = requests.post(f"{TOKEN_URL}/generate", json=data_payload)
    response_json = response.json()

    # sent ok reponse
    return jsonify({
        "message":"success",
        "data": {
            "token":response_json["token"],
            "expired_at":response_json["expired_at"]
        }
    }), 200
@app.route("/list", methods=["GET"])
def user_list():
    """_summary_

    Returns:
        _type_: _description_
    """
    auth = None
    if 'Authorization' in request.headers:
        auth = request.headers['Authorization']
    if not auth:
        return jsonify({
            "message":"Token is missing !!"
        }), 401
    auth = request.headers['Authorization'].split(' ')
    token = auth[1]
    # hit validate token
    data_payload = {
        "token" : token
    }
    response = None
    try:
        response = requests.post(f"{TOKEN_URL}/validate", json=data_payload)
    except requests.exceptions.RequestException as exception:  # This is the correct syntax
        return jsonify({
            "message":f"{exception}"
        }), 400
    if response.status_code == 401 :
        return jsonify({
            "message":"please re-login un-authorized"
        }), 401
    # hit get list users
    try:
        response = requests.get(f"{USER_URL}/list")
    except requests.exceptions.RequestException as exception:  # This is the correct syntax
        return jsonify({
            "message":f"{exception}"
        }), 400
    response_json = response.json()

    return jsonify({
        "message":"success",
        "data" : response_json["data"]
    }), 200
if __name__ == "__main__":
    JSONExceptionHandler(app)
    app.run(host=HOST, port=PORT)
    