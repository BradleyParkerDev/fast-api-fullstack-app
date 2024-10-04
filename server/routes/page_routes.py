from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

# Page Views
class PageRoutes:
    def __init__(self):
        self.router = APIRouter()

    def setup_routes(self):
        @self.router.get("/")
        async def root(request: Request):
            return templates.TemplateResponse("/pages/index.html", {"request": request})

        @self.router.get("/user")
        async def user_page(request: Request):
            return templates.TemplateResponse("/pages/user_page/user_page.html", {"request": request})

        @self.router.get("/user/{id}")
        async def authenticated_user_page(request: Request, id: str):
            return templates.TemplateResponse("/pages/authenticated_user_page/authenticated_user_page.html", {
                "request": request,
                "user_id": id
            })

        return self.router
