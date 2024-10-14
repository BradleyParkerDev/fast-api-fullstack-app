import bcrypt
from fastapi import Request
from lib import AuthSessionHelper, AuthTokenHelper
from database.models import User, UserSession

# Auth Util
class AuthUtility:
    
    def __init__(self):
        self.session = AuthSessionHelper()   
        self.token = AuthTokenHelper()     


    # Hash Password
    def generate_hash_password(self, new_password, salt_rounds):
        # The password should be used directly without hardcoding
        # Ensure that the password is in bytes
        new_password = new_password.encode('utf-8')
        
        # Custom number of salt rounds (e.g., 5 rounds)
        salt = bcrypt.gensalt(rounds=salt_rounds)

        # Hash the password with the custom salt rounds
        hashed_password = bcrypt.hashpw(new_password, salt)

        print(f"hashed_password: {hashed_password}")

        # Decode hashed_password if necessary (assuming database expects a string)
        if isinstance(hashed_password, bytes):
            hashed_password = hashed_password.decode('utf-8')               
        return hashed_password



    # Validate Password
    def validate_password(self, password, hashed_password):
        # hashed_password should already be in bytes, so don't encode it again
        if isinstance(hashed_password, str):
            hashed_password = hashed_password.encode('utf-8')
        
        print(f"hashed_password: {hashed_password}")
        
        # Verify the password
        if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
            return True
        else:
            return False
        
    
    
    # Middleware - Authorize User
    async def authorize_user(self, request: Request, call_next):
        print("Authorization Middleware!!!")
        
        # Get the session token from cookies
        session_token = request.cookies.get('session_cookie')
        
        print(f"session_token: {session_token}")
        
        # Decode the token (assuming token verification method is async)
        decoded_token = self.token.verify_session_token(session_token)
        
        # Perform the rest of your authorization logic here...
        # For now, we're assuming the user is authorized for demo purposes.
        
        # Continue processing the request if the user is authorized
        response = await call_next(request)
        
        return response

        
