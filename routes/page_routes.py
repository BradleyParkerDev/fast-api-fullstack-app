from fastapi import APIRouter, Request,Response
from fastapi.templating import Jinja2Templates
from controllers.pages import home_page_controller, user_page_controller, authenticated_user_page_controller
templates = Jinja2Templates(directory="resources/templates")

# Page Views
class PageRoutes:
    def __init__(self):
        self.router = APIRouter()

    def setup_routes(self):
        @self.router.get("/")
        async def home_page(request: Request, response:Response):
            return home_page_controller(request,response)

        @self.router.get("/user")
        async def user_page(request: Request, response:Response):
            return user_page_controller(request,response)

        @self.router.get("/user/{user_name}")
        async def authenticated_user_page(request: Request, response:Response, user_name: str):
            return authenticated_user_page_controller(request,response,user_name)


        return self.router
