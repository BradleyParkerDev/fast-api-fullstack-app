import bcrypt
from fastapi import Request, Response
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
        
        # If there is a session decode its token
        if session_token:
            print(f"session_token: \n{session_token}")
            
            # Decode the token (assuming token verification method is async)
            decoded_token = self.token.verify_session_token(session_token)
            
            print(f"decoded_token: \n{decoded_token}")
            # Perform the rest of your authorization logic here...
            # For now, we're assuming the user is authorized for demo purposes.
            
            # Store the decoded token in request.state
            request.state.decoded_token = decoded_token
            
            response = await call_next(request) 
            

              
        # If there is not a token, create one
        else:

            guest_session = self.session.create_user_session()
            
            # create dict with session information
            guest_session_payload = {
                "session_id": str(guest_session.session_id),
                "last_updated": guest_session.last_updated.isoformat()  # Convert datetime to string
            }
            
            guest_session_token = self.token.generate_session_token(guest_session_payload)

            # Create a response and set a cookie
            # response = Response()
                    # Continue processing the request if the user is authorized
            response = await call_next(request)  
            response.set_cookie(key="session_cookie", value = guest_session_token, httponly=True)
            

        
        return response
               
            