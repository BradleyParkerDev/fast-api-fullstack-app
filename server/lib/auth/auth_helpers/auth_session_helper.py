from database.models import UserSession
from database import DB

class AuthSessionHelper:
    
    def __init__(self):
        self.session_id = None
        self.user_id = None
     
     
     
     
    # Session Methods
    def create_user_session(self, user_id):
        db = DB()
        db.initialize()
        
        user_session = UserSession()
        
        
        
        # If user is logging in add their user_id to the session
        if user_id:
            user_session.user_id = user_id
            
        
        
        db.session.add(user_session)
        
        db.session.commit()
        print(f"user_session session_id: {user_session.session_id}")
        return user_session

        
        # return 'User session created!'
    
    def get_current_session():
        return 'Session id in cookies match session on server!'
    
    def delete_user_session():
        return 'User session deleted!'
    
    def create_session_cookie(self):
        return 'cookie'
    
    def remove_session_cookie_from_headers():
        return ''
    
    

     
       
    def remove_expired_sessions():
        return 'Expired sessions removed!'