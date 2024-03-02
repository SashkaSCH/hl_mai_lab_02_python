from . import ma
from .models import User, Wall, Message

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        sqla_session = db.session
        load_instance = True

class WallSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Wall
        sqla_session = db.session
        load_instance = True

class MessageSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Message
        sqla_session = db.session
        load_instance = True
