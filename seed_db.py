from database.db import get_session
from database.models.user import User
from datetime import datetime

# Get a session
db = get_session()

# Create some sample users
user1 = User(
    first_name="John",
    last_name="Doe",
    email_address="john.doe@example.com",
    user_name="johndoe",
    password="securepassword",
    last_updated=datetime.utcnow()
)

user2 = User(
    first_name="Jane",
    last_name="Doe",
    email_address="jane.doe@example.com",
    user_name="janedoe",
    password="anothersecurepassword",
    last_updated=datetime.utcnow()
)

# Add users to the session and commit the transaction
db.add(user1)
db.add(user2)
db.commit()

# Close the session
db.close()
