from database.models import UserSession
from database import DB

class SessionUtility:
    
    def __init__(self):
        self.session_id = None
        self.user_id = None
        self.db = DB()
     
     
     
     
    # Session Methods
    def create_user_session():
        return 'User session created!'
    
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