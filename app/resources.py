from flask import request
from flask_restful import Resource, Api
from .models import db, User, Wall, Message
from .schemas import UserSchema, WallSchema, MessageSchema

user_schema = UserSchema()
users_schema = UserSchema(many=True)
wall_schema = WallSchema()
walls_schema = WallSchema(many=True)
message_schema = MessageSchema()
messages_schema = MessageSchema(many=True)

class UserResource(Resource):
    def get(self, id=None):
        if id:
            user = User.query.get(id)
            return user_schema.dump(user)
        else:
            users = User.query.all()
            return users_schema.dump(users)

class WallResource(Resource):
    def get(self, id=None):
        if id:
            wall = Wall.query.get(id)
            return wall_schema.dump(wall)
        else:
            walls = Wall.query.all()
            return walls_schema.dump(walls)

class MessageResource(Resource):
    def get(self, id=None):
        if id:
            message = Message.query.get(id)
            return message_schema.dump(message)
        else:
            messages = Message.query.all()
            return messages_schema.dump(messages)

def setup_routes(app):
    api = Api(app)
    api.add_resource(UserResource, '/users', '/users/<int:id>')
    api.add_resource(WallResource, '/walls', '/walls/<int:id>')
    api.add_resource(MessageResource, '/messages', '/messages/<int:id>')
