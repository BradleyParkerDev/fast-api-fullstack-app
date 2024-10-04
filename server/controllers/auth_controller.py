import json
from fastapi import Request, HTTPException, status
from fastapi.responses import RedirectResponse
from lib import AuthUtility, SessionUtility
from database.models import User, UserSession
from database import DB

class AuthController:
    
    def __init__(self):
        self.auth_util = AuthUtility()
        self.session_util = SessionUtility()
        self.db = DB()
        
    async def login_user(self, request:Request):
        body = await request.json()
        print(body)
        
        
        # find user
        # validate password
        passwords_match = self.auth_util.validate_password(body)
        
        # if passords_match 
        # create user session
        self.session_util.create_user_session()
        
        
        # redirect to authenticated_user_page
        
        
        
        
        return "User successfully logged in!"
    
    async def logout_user(self, request:Request):
        
        self.session_util.delete_user_session()
        
        # redirect to index page
        
        
        return 'User successfully logged out!'