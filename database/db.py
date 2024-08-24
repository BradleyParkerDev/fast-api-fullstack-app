import os
from dotenv import load_dotenv
from sqlmodel import SQLModel, create_engine, Session


load_dotenv()

LOCAL_DATABASE_URL = os.getenv("LOCAL_DATABASE_URL")

engine = create_engine(LOCAL_DATABASE_URL)

def init_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    return Session(engine)