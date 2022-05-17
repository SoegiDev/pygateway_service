from flask import Flask, request, jsonify
import json
import jwt
from datetime import timezone
import datetime
import os
from dotenv import load_dotenv
from JSONExceptionHandler import JSONExceptionHandler
import socket
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, './.env'))

app = Flask(__name__)
HOST = "0.0.0.0"
PORT = 5003
ENV = os.environ.get('FLASK_ENV')
secret_key = os.environ.get('SECRET_KEY')
secret_key_refresh = os.environ.get('SECRET_KEY_REFRESH')
expire_token = os.environ.get('JWT_ACCESS_TOKEN_EXPIRES')
expired_token_refresh = os.environ.get('JWT_REFRESH_TOKEN_EXPIRES')
dict_access = {}
@app.route("/",methods=["GET"])
def home():
    test=  os.environ.get("FLASK_ENV")
    return f'TOKEN MODE: {test} SOCKETNAME: {socket.gethostname()}'

@app.route("/generate",methods=["POST"])
def generate():
    payload = json.loads(request.data)
    publicid = payload["id"]
    datauser = {"public_id":publicid}
    token = createToken(datauser)
    refresh = createRefreshToken(datauser)
    checkKey(dict_access,publicid,0)
    return jsonify({
        "token":token,
        "token_refresh":refresh
    })

    
def createToken(dataUser : object):
    print("Expired ",expire_token)
    token = jwt.encode({
            'id': dataUser['public_id'],
            'exp' : datetime.datetime.utcnow() + datetime.timedelta(hours = int(expire_token))
        }, secret_key, algorithm='HS256')
    return token

def createRefreshToken(dataUser : object):
    token = jwt.encode({
            'id': dataUser['public_id'],
            'exp' : datetime.datetime.utcnow() + datetime.timedelta(days = int(expired_token_refresh))
        }, secret_key_refresh, algorithm='HS256')
    return token

@app.route("/validate",methods=["POST"])
def validate():
    payload = json.loads(request.data)
    token = payload["token"]
    publicid = ''
    try:
        expired_at = datetime.datetime.utcnow() + datetime.timedelta(seconds=30)
        jwt_decoded = jwt.decode(token,secret_key, algorithms=["HS256"])
        publicid = jwt_decoded["id"]
        checkKey(dict_access,publicid,0)
        return jsonify({
            "id":jwt_decoded["id"]
        }), 200
    except Exception as err:
        ch = checkKey(dict_access,publicid,1)
        if ch:
            return jsonify({ "message" : "un-authorized" }), 401
        else:
            return jsonify({ "message" : "please re-login un-authorized ..." }), 401
        #return jsonify({ "message" : "un-authorized" }), 401

@app.route("/refresh",methods=["POST"])
def validate_refresh():
    payload = json.loads(request.data)
    token = payload["token"]
    publicid = ''
    try:
        jwt_decoded = jwt.decode(token, secret_key_refresh, algorithms=["HS256"])
        publicid = jwt_decoded["id"]
        datauser = {'public_id':jwt_decoded["id"]}
        token = createToken(datauser)
        refresh = createRefreshToken(datauser)
        checkKey(dict_access,publicid,0)
        return jsonify({
                "token":token,
                "token_refresh":refresh
            }), 200
    except Exception as err:
        ch = checkKey(dict_access,publicid,1)
        if ch:
            return jsonify({ "message" : "un-authorized" }), 401
        else:
            return jsonify({ "message" : "please re-login un-authorized ..." }), 401


def checkKey(dict, id,typ = 0):
    if id in dict.keys():
        if dict.get(id) > 2 :
            print(dict_access.get(id))
            return False
        else:
            count = 0
            if typ == 0:
                count = 0
                dict.update({id:count})
                print(dict_access.get(id))
            elif typ > 0:
                x = dict_access.get(id)
                count = x+1
                dict.update({id:count})
                print(dict_access.get(id))
            return True
    else:
        count = 0
        dict_access[id] = count+1
        print(dict_access.get(id))
        return True

if __name__ == "__main__":
    JSONExceptionHandler(app)
    if ENV =='development':
        app.run(host=HOST, port=PORT, debug=1)
    else:
        app.run(host=HOST, port=PORT, debug=0)
        