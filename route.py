from service import userService
import socket
from flask import current_app,Blueprint
v1 = Blueprint('api_v1', __name__, url_prefix='/v1')


@v1.route("/login",methods=["POST"])
def user_login():
    return userService.login()

@v1.route("/initial",methods=["GET"])
def initial_user_db():
    return userService.initial_user_db()

@v1.route("/register",methods=["POST"])
def user_register():
    return userService.register()

@v1.route("/refresh",methods=["POST"])
def user_token_refresh():
    return userService.refresh()

@v1.route("/login_ldap",methods=["POST"])
def user_login_ldap():
    return userService.login_ldap()

@v1.route("/list_user",methods=["GET"])
def user_list():
    return userService.user_list()

@v1.route("/home",methods=["GET"])
def home():
    """_summary_

    Returns:
        _type_: _description_
    """
    test=  current_app.config.get("FLASK_ENV")
    return f'GATEWAY INI ADALAH MODE: {test} SOCKETNAME: {socket.gethostname()}'
