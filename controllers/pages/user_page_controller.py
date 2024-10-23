import os
from fastapi import Request, Response
from fastapi.templating import Jinja2Templates
from lib import LayoutUtility
from dotenv import load_dotenv
templates = Jinja2Templates(directory="resources/templates")

# Load environment variables from .env file
load_dotenv()
DEBUG = os.getenv("DEBUG")




layout = LayoutUtility()


def user_page_controller(request:Request, response:Response):



    return templates.TemplateResponse("/pages/user_page/user_page.html", {
        "request": request,
        "webpack" :  layout.webpack,
        "DEBUG" : DEBUG,
        "hotreload" : layout.arel.hotreload     
    })