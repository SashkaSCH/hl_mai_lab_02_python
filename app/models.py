from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(255), unique=True, nullable=False)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    title = db.Column(db.String(255))
    password = db.Column(db.String(255), nullable=False)
    photo = db.Column(db.LargeBinary)

class Wall(db.Model):
    wall_id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    description = db.Column(db.Text)
    update_date = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

class Message(db.Model):
    message_id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    recipient_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    message_date = db.Column(db.DateTime, server_default=db.func.now())
