import json
from fastapi import Request, HTTPException, status
from lib import AuthUtility
from database.models import User
from database import DB

# CRUD operations on User
class UserController:
    def __init__(self):
        self.auth_util = AuthUtility()

        
    # Register User
    async def register_user(self, request: Request):
        request_body = await request.json()
        print(f"first name: {request_body['first_name']}")
        first_name = request_body.get('first_name')
        print(first_name)
        

        first_name = request_body.get('first_name')
        last_name = request_body.get('last_name')
        email_address = request_body.get('email_address')
        user_name = request_body.get('user_name')
        password = request_body.get('password')
        
        
        db = DB()
        db.initialize()
        
        
        
        hashed_password =  self.auth_util.generate_hash_password(password, 5)
        # new_user = User(body['email_address'], hashed_password)
             

        try:
            # Create a new User instance
            new_user = User(
                first_name=first_name,
                last_name=last_name,
                email_address=email_address,
                user_name=user_name,
                password=hashed_password
            )

            # Add the new user to the session
            db.session.add(new_user)

            # Commit the transaction to save the user to the database
            db.session.commit()

            return {"message": "User registered successfully"}

        except Exception as e:
            db.session.rollback()  # Rollback in case of any error
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        
        finally:
            db.close()  # Ensure the session is closed
        
        
        
        
        
        
        return "user registered"
    
    # Get User
    async def get_user(self, request: Request):
        
        db = DB()
        db.initialize()
        
        
        found_user = db.session.query(User).filter()
        
        return "user data retrieved"

    # Update User
    async def update_user(self, request: Request):
        return "user updated"
    
    # Delete User

    async def delete_user(self, request: Request):
        return "user deleted"
            
