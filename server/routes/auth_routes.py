import json
from fastapi import APIRouter, Request
from controllers import AuthController
from database.models import User, UserSession
from database import DB

# Auth API
class AuthRoutes:
    def __init__(self):
        self.router = APIRouter()
        self.auth_controller = AuthController()
        self.db = DB()
    
    def setup_routes(self):
        
        # Login User
        @self.router.post("/api/auth/login-user")   
        async def login_user(request:Request):
            return await self.auth_controller.login_user(request)
    
        # Logout User
        @self.router.post("/api/auth/logout-user")   
        async def logout_user(request:Request):
            return await self.auth_controller.logout_user(request)
         
        return self.router
    
    
