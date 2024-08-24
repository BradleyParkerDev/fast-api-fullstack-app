from fastapi import Request

class UserController:

    # Register User
    async def register_user(self, request: Request):
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
            
