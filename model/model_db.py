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

class Tasks(Base):
    __tablename__ = 'tasks_user'
    
    id = Column(Integer, primary_key=True)
    id_user = Column(Integer)
    title = Column(String)
    description = Column(String)    

engine = create_engine(config.tg_bot.db_url, echo=True)  
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session();    

def create_user_from_dict(data: dict):
    user = User(**data)
    session.add(user)
    session.commit()

def get_user(user_id):
    return session.query(User).filter(User.tg_id == user_id).first()    

def delete_user(user_id: int):
    user = session.query(User).filter(User.tg_id == user_id).first()
    if user:
        session.delete(user)
        session.commit()
        return True
    return False        

def get_task_first(id: int):
    return session.query(Tasks).filter(Tasks.id == id).first()

def get_task_all(user_id: int):
    return session.query(Tasks).filter(Tasks.id_user == user_id).all()

def create_task_from_dict(data: dict):
    task = Tasks(**data)
    session.add(task)
    session.commit()

def view_tasks(user_id: int):
    tasks = get_task_all(user_id)
    return tasks

def delete_tasks(id: int):
    task = get_task_first(id)
    if (task):
        session.delete(task)
        session.commit()
        return True
    return False    

def update_task_title (id: int, title_text: str):
    task = get_task_first(id)
    if task: 
        task.title = title_text
        session.commit()
        return True
    return False

def update_task_description (id: int, description_text: str):
    task = get_task_first(id)
    if task: 
        task.description = description_text
        session.commit()
        return True
    return False    