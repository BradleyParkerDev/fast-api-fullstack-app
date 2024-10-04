import bcrypt
from lib import SessionUtility, Middleware
from database.models import User, UserSession

# Auth Util
class AuthUtility:
    
    def __init__(self):
        self.middleware = Middleware.authorize_user()
        self.session = SessionUtility()

    
    
    # Password Methods
    def generate_hash_password(self, new_password, salt_rounds):
        
        # Custom number of salt rounds (e.g., 5 rounds)
        salt = bcrypt.gensalt(rounds=salt_rounds)

        # Hash the password with the custom salt rounds
        hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), salt)
        
        return hashed_password
   
   
   
   
   
    def validate_password(self, password, hashed_password):
        
        # Verify the password
        if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
            return True
        else:
            return False
        


    
