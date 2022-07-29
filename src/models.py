import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(150), nullable=False)
    email = Column(String(50), nullable = False)
    password = Column(String(25), nullable = False, unique = True)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    photo_url = Column(String())
    user_id = Column(Integer, ForeignKey("user.id"), nullable = False )
    
    def to_dict(self):
        return {}

class Favorite(Base):
    __tablename__ = 'favorite'
    post_id = Column(Integer, ForeignKey("post.id"), nullable = False, primary_key=True )
    user_id = Column(Integer, ForeignKey("user.id"), nullable = False, primary_key=True )

class Comentaries(Base):
    __tablename__ = 'comentaries'
    id = Column(Integer, primary_key=True)
    description = Column(String(200))
    post_id = Column(Integer, ForeignKey("post.id"), nullable = False )
    user_id = Column(Integer, ForeignKey("user.id"), nullable = False )


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')