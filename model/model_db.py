from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker;

Base = declarative_base()

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

engine = create_engine('postgresql+psycopg2://postgres:Roman13_D14AR@localhost:5432/reminder_bot')    

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session();    

new_user = User(
    tg_id=123456,
    username='test_user',
    name_user='Ivan',
    surname_user='Ivanov',
    age_user=25,
    login_user='ivan123',
    password_user='securepass'
)

session.add(new_user)
session.commit()