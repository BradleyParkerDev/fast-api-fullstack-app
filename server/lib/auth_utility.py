from lib import SessionUtility
from database.models import User, UserSession
from database import DB

# Auth Util
class AuthUtility:
    
    def __init__(self):
        self.user_authenticated = False
        self.session = SessionUtility()
        self.db = DB()
    
    def auth_check():
        # if user_session has user_id AND cookie has user_id
        #return user_authenticated true and user_id
        return 


    # Password Methods
    def hash_password(self, new_password):
        return 'Password hashed!'
   
    async def validate_password(self, current_password):
        await print('Password matches password on server!')
        return 

    
    def middleware():

        # get cookie from headers
        print('Middleware!!!') 
