import os
from dotenv import load_dotenv
from fastapi import Request, Response
from fastapi.templating import Jinja2Templates
from lib import LayoutUtility

templates = Jinja2Templates(directory="resources/templates")

# Load environment variables from .env file
load_dotenv()
DEBUG = os.getenv("DEBUG")



layout = LayoutUtility()


def authenticated_user_page_controller(request:Request, response:Response, id:str):



    
    return templates.TemplateResponse("/pages/authenticated_user_page/authenticated_user_page.html", {
        "request": request,
        "user_id": id,
        "webpack" :  layout.webpack,
        "DEBUG" : DEBUG,
        "hotreload" : layout.arel.hotreload     
    })