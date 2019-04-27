from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
CORS(app)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.route('/')
def health():
    res = {'status': 'UP'}
    return jsonify(res)


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    user = User.query.filter_by(username=data['username']).first()
    if user is None or not user.check_password(data['password']):
        return jsonify({'status':'fail'}), 404

    return jsonify({'token': 'supersecret', 'user':{'name': user.username, 'usertype': user.usertype}}), 200


@app.route('/event', methods=['GET'])
def get_events():
    # get all events
    return jsonify({'status':'success'}), 200


@app.route('/event', methods=['POST'])
def create_event():
    
    return jsonify({'status':'success'}), 201


@app.route('/event', methods=['PUT'])
def edit_event():

    return jsonify({'status':'success'}), 200


@app.route('/gps', methods=['POST'])
def gps():
    # receive gps location
    # check if gps location is within event range
    # respond with any events
    return jsonify({'status':'success'}), 200


@app.route('/images/<path:path>', methods=['GET'])
def get_image(path):
    return send_from_directory('images', path)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    usertype = db.Column(db.String(64))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
