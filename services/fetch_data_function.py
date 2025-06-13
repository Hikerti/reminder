import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from model.model_db import session, Task

def get_task_first(id: int):
    return session.query(Task).filter(Task.id == id).first()

def get_task_all(user_id: int):
    return session.query(Task).filter(Task.id_user == user_id).all()