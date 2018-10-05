import jwt
import datetime
from flask import jsonify, request
from app import app
from app.accounts import Account
from instance.config import Config
from functools import wraps

new_account = Account()


@app.route('/todo/api/v1/auth/register', methods=['POST'])
def register():
    if 'username' not in request.json or 'email_address' not in request.json or 'password' not in request.json:
        return jsonify({"message": "please type in the username, email address and password"}), 400
    data = request.get_json()
    username = data['username']
    email_address = data['email_address']
    password = data['password']
    if not username:
        return jsonify({"message": "username required"}), 400
    if not email_address:
        return jsonify({"message": "Email address required"}), 400
    if not password:
        return jsonify({"message": "password required"}), 400
    if isinstance(username, int) or isinstance(username, float) or isinstance(username, list):
        return jsonify({"message": "Please enter a string"}), 400
    if isinstance(email_address, int) or isinstance(email_address, float) or isinstance(email_address, list):
        return jsonify({"message": "Please enter a string"}), 400
    if isinstance(password, int) or isinstance(password, float) or isinstance(password, list):
        return jsonify({"message": "Please enter a string"}), 400
    if not new_account.validate_username(username):
        return jsonify({"message": "The username should not be less than 4 characters and have no whitespaces"}), 400
    if not new_account.validate_email_address(email_address):
        return jsonify({"message": "The email should follow the format of valid emails (johndoe@mail.com)"}), 400
    if not new_account.validate_password(password):
        return jsonify(
            {
                "message": "The password should not be "
                           "less than 4 characters and should contain "
                           "A capital letter, a small letter, a digit and a special character."
            }
        ), 400
    if new_account.check_user(username, email_address, password):
        return jsonify({"message": "User already exists"}), 409
    else:
        new_account.register(username, email_address, password)
        return jsonify({"message": "You've been successfully registered"}), 201


@app.route('/todo/api/v1/auth/login', methods=['POST'])
def login():
    authorize = request.authorization
    username = authorize.username
    password = authorize.password
    if not new_account.check_username(username):
        return jsonify({"message": "User does not exist, please register"}), 400
    if not new_account.check_password(password):
        return jsonify({"message": "Invalid password, please try again"}), 400
    else:
        token = jwt.encode(
            {
                "username": username,
                "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=24)
            },
            Config.SECRET_KEY
        )
        return jsonify(
            {
                "token": token.decode("UTF-8"),
                "message": "You have successfully logged in"
            }
        ), 200


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return jsonify({"message": "Token is missing"}), 401
        try:
            data = jwt.decode(token, Config.SECRET_KEY)
            current_user = new_account.get_user(username=data['username'])
        except jwt.DecodeError:
            return jsonify({"message": "Token is invalid"}), 401
        except jwt.ExpiredSignatureError:
            return jsonify({"message": "Token has expired"}), 401
        return f(current_user, *args, **kwargs)

    return decorated
