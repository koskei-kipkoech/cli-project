import sys 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, TM, Student

DATABSE_URL = "sqlite://tms.db"

engine = create_engine(DATABSE_URL)
Session = sessionmaker(bind=engine)
session = Session()

def init_db():
    #initialize database
    Base.metadata.create_all(engine)
    print("Database initialized successfully.")

def create_tm():
    #create a new TM
    name = input("Enter the Tm Name: ")
    email = input("Enter the Tm Email: ")
    tm = TM(name=name, email=email)
    session.add(tm)
    session.commit()
    print(f"TM '{name}' with ID {tm.id} created successfully.")

