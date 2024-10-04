from fastapi import APIRouter, Request
from database.models import User

from controllers import UserController


# User API
class UserRoutes:
    def __init__(self):
        self.router = APIRouter() 
        self.user_controller = UserController()  # Instantiate the controller

        
    def setup_routes(self):

        # Register User
        @self.router.post("/api/users/register-user")
        async def register_user(request: Request):
            return await self.user_controller.register_user(request)

        
        # Get User
        @self.router.get("/api/users/get-user")
        async def get_user(request: Request):
            return await self.user_controller.get_user(request)


        # Update User
        @self.router.put("/api/users/update-user")
        async def update_user(request: Request):
            return await self.user_controller.update_user(request)

        
        # Delete User
        @self.router.delete("/api/users/delete-user")
        async def delete_user(request: Request):
            return await self.user_controller.delete_user(request)

        return self.router         
