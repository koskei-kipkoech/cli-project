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


def update_tm():
    tm_id = int(input("Enter the ID to update: "))
    tm = session.get(TM, tm_id)
    if not tm:
        print(f"TM with ID {tm_id} not found.")
        return
    tm.name =  input(f"Enter new name for TM (current : {tm.name}): ") or tm.name
    tm.email = input(f"Enter new email for TM (current : {tm.email}):") or tm.email
    session.commit()
    print(f"TM with ID {tm_id} updated successfully.")


def delete_tm():