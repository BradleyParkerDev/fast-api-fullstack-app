import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models.user import User, Base  # Import Base along with your model

load_dotenv()

# Load the database URL from environment variables
LOCAL_DATABASE_URL = os.getenv("LOCAL_DATABASE_URL")
# TEST_DATABASE_URL = os.getenv("TEST_DATABASE_URL", "sqlite:///./test.db")

# Set up the SQLAlchemy engine
engine = create_engine(LOCAL_DATABASE_URL, echo=True)
# engine = create_engine(TEST_DATABASE_URL, echo=True)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    """Initialize the database and create tables."""
    print(f"Connecting to database at {LOCAL_DATABASE_URL}")
    
    # Create tables based on the Base metadata
    Base.metadata.create_all(bind=engine)
    
    print("Tables created successfully!")

# Optional: Provide a session for interacting with the database
def get_session():
    """Provide a database session."""
    return SessionLocal()
