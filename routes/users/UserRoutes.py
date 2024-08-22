from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

class UserRoutes:
    def __init__(self):
        self.router = APIRouter()
    
    def setup_routes(self):

        # Register User
        @self.router.post("/api/users/register-user")
        async def register_user(request: Request):
            return "user registered"
        
        # Get User
        @self.router.get("/api/users/get-user")
        async def get_user(request: Request):
            return "user data retrieved"

        # Update User
        @self.router.put("/api/users/update-user")
        async def update_user(request: Request):
            return "user updated"
        
        # Delete User
        @self.router.delete("/api/users/delete-user")
        async def delete_user(request: Request):
            return "user deleted"
                
