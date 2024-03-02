from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    login = Column(String(256), unique=True)
    first_name = Column(String(256))
    last_name = Column(String(256))
    birth_date = Column(DateTime)
    email = Column(String(256))
    title = Column(String(256))
    password = Column(String(256))
    photo = Column(String(256))

    walls = relationship("Wall", back_populates="user")
    messages_sent = relationship("Message", foreign_keys=[message_id], back_populates="author")
    messages_received = relationship("Message", foreign_keys=[recipient_id], back_populates="recipient")


class Wall(Base):
    __tablename__ = "walls"

    wall_id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(String(256))
    user_id = Column(Integer, ForeignKey("users.id"))
    description = Column(String(256))
    update_date = Column(DateTime)

    user = relationship("User", back_populates="walls")


class Message(Base):
    __tablename__ = "messages"

    message_id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(String(256))
    author_id = Column(Integer, ForeignKey("users.id"))
    recipient_id = Column(Integer, ForeignKey("users.id"))
    message_date = Column(DateTime)

    author = relationship("User", foreign_keys=[author_id], back_populates="messages_sent")
    recipient = relationship("User", foreign_keys=[recipient_id], back_populates="messages_received")
