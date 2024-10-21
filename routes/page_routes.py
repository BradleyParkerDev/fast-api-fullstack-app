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

        @self.router.get("/user/{id}")
        async def authenticated_user_page(request: Request, response:Response, id: str):
            return authenticated_user_page_controller(request,response,id)


        return self.router
