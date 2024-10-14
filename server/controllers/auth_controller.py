import json
from fastapi import Request, Response, HTTPException, status
from fastapi.responses import RedirectResponse
from lib import AuthUtility
from database.models import User, UserSession
from database import DB


# Controller operations for the /api/auth
class AuthController:
    
    def __init__(self):
        self.auth_util = AuthUtility()
       
        
    async def login_user(self, request:Request, response:Response):
        # Retrieve and parse the request body
        request_body = await request.json()

        # Extract email and password from the request
        email_address = request_body.get('email_address')
        password = request_body.get('password')

        # Ensure both email and password are provided
        if not email_address or not password:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Missing email or password")

        # Initialize the DB after retrieving the request body
        
        db = DB()
        db.initialize()
        
        # Find user in database
        found_user = db.session.query(User).filter(User.email_address == email_address).first()
        
        
        # find user
        # validate password
        passwords_match = self.auth_util.validate_password(password, found_user.password)
        
        print(f"Passwords match: {passwords_match}")
        
        if passwords_match: 
        # create user session
            user_session = self.auth_util.session.create_user_session(found_user.user_id)
            # Assuming user_session is an object or Pydantic model, you need to convert it to a dict
            session_payload = {
                "user_id": str(user_session.user_id),  # Make sure values are serializable
                "session_id": str(user_session.session_id),
                "last_updated": user_session.last_updated.isoformat()  # Convert datetime to string
            }
            session_token = self.auth_util.token.generate_session_token(session_payload)
        
        
        # redirect to authenticated_user_page
        
        
        db.close()
        # Create session_cookie
        response.set_cookie(key="session_cookie", value=session_token, httponly=True)       
                 
        return "User successfully logged in!"
    
    def logout_user(self, request:Request):
        
        self.auth_util.session.delete_user_session()
        
        # redirect to index page
        
        
        return 'User successfully logged out!'