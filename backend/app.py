from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash
import json
import dateutil.parser as parser
from marshmallow import Schema, fields

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

    user_interests = []
    for interest in user.interests:
        user_interests.append({'id': interest.id, 'name': interest.name})

    res = {
        'token': 'supersecret',
        'user': {
                'name': user.username,
                'user_type': user.user_type,
                'interests': user_interests
            }
        }

    return jsonify(res), 200


@app.route('/event', methods=['GET'])
def get_events():
    events = db.session.query(Event).all()

    payload = []
    for e in events:
        id = e.id
        name = e.name
        description = e.description
        location = e.location
        url_info = e.url_info
        geo_fence = json.loads(e.geo_fence)
        date = e.date
        event_type = e.event_type.name
        payload.append({'id': id, 'name':name,'description':description,'location':location,'url_info':url_info,'geo_fence':geo_fence,'date':date,'event_type':event_type})
 
    return jsonify(payload), 200


@app.route('/event', methods=['POST'])
def create_event():
    data = request.get_json()

    event_type = EventType.query.filter_by(name=data['event_type']).first()

    if event_type is None:
        return jsonify({'status':'fail', 'message': 'Invalid event type'}), 400

    event = Event(
        name = data['name'],
        description = data['description'],
        location = data['location'],
        url_info = data['url_info'],
        geo_fence = json.dumps(data['geo_fence']),
        date = data['date'],
        event_type_id = event_type.id
    )

    db.session.add(event)
    db.session.commit()

    return jsonify({'status':'success'}), 201


@app.route('/event', methods=['PUT'])
def edit_event():
    data = request.get_json()
    
    event = Event.query.get(data['id'])

    if event is None:
        return jsonify({'status':'fail', 'message': 'Event id does not exist'}), 400

    event_type = EventType.query.filter_by(name=data['event_type']).first()

    if event_type is None:
        return jsonify({'status':'fail', 'message': 'Invalid event type'}), 400

    event.name = data['name']
    event.description = data['description']
    event.location = data['location']
    event.url_info = data['url_info']
    event.geo_fence = json.dumps(data['geo_fence'])
    event.date = data['date']
    event.event_type_id = event_type.id
    
    db.session.commit()

    return jsonify({'status':'success'}), 200


@app.route('/eventTypes', methods=['GET'])
def get_event_types():
    event_types = db.session.query(EventType).all()
    schema = EventTypeSchema(many=True)
    payload = schema.dump(event_types)[0]
    return jsonify(payload), 200


@app.route('/gps', methods=['POST'])
def gps():
    # receive gps location
    # check if gps location is within event range
    # respond with any events
    return jsonify({'status':'success'}), 200


@app.route('/images/<path:path>', methods=['GET'])
def get_image(path):
    return send_from_directory('images', path)

interests = db.Table('interests', db.Model.metadata,
    db.Column('user', db.Integer, db.ForeignKey('user.id')),
    db.Column('event_type', db.Integer, db.ForeignKey('event_type.id'))
)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    user_type = db.Column(db.String(64))
    interests = db.relationship("EventType", secondary=interests)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class EventType(db.Model):
    __tablename__ = 'event_type'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    events = db.relationship('Event', backref='event', lazy=True)


class Event(db.Model):
    __tablename__ = 'event'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    description = db.Column(db.String(200))
    location = db.Column(db.String(200))
    url_info = db.Column(db.String(200))
    geo_fence = db.Column(db.String(200))
    date = db.Column(db.String(200))
    event_type_id = db.Column(db.Integer, db.ForeignKey('event_type.id'), nullable=False)
    event_type = db.relationship('EventType', backref='event_type', lazy=True)

class EventTypeSchema(Schema):
    id = fields.Int()
    name = fields.Str()


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
