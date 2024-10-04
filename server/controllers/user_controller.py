import json
from fastapi import Request, HTTPException, status
from lib import AuthUtility
from database.models import User
from database import DB

# CRUD operations on User
class UserController:
    def __init__(self):
        self.auth_util = AuthUtility()
        self.db = DB()
        
    # Register User
    async def register_user(self, request: Request):
        body = await request.json()
        print(f"first name: {body}")
        firstName = body.get('firstName')
        print(firstName)
        hashed_password = self.auth_util.hash_password()
        new_user = User(body['email_address'], hashed_password)
        return "user registered"
    
    # Get User
    async def get_user(self, request: Request):
        return "user data retrieved"

    # Update User
    async def update_user(self, request: Request):
        return "user updated"
    
    # Delete User

    async def delete_user(self, request: Request):
        return "user deleted"
            
