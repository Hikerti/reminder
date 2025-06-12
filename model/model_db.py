from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker;

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config.config import Config, load_config

Base = declarative_base()

config: Config = load_config() 
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    tg_id = Column(Integer, unique=True)
    username = Column(String)
    name_user = Column(String)
    surname_user = Column(String)
    age_user = Column(Integer)
    login_user = Column(String)
    password_user = Column(String)

class Task(Base):
    __tablename__ = 'tasks'
    
    id = Column(Integer, primary_key=True)
    id_task = Column(Integer)
    id_user = Column(Integer)
    title = Column(String)
    description = Column(String)    

engine = create_engine(config.tg_bot.db_url, echo=True)  

Session = sessionmaker(bind=engine)
session = Session();    

def create_user_from_dict(data: dict):
    user = User(**data)
    session.add(user)
    session.commit()

def create_task_from_dict(data: dict):
    task = Task(**data)
    session.add(task)
    session.commit()

def view_tasks(user_id: int):
    tasks = session.query(Task).filter(Task.id_user == user_id).all()
    return tasks
