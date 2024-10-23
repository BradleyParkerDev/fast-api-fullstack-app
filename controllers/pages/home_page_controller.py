import os
from dotenv import load_dotenv
from fastapi import Request, Response
from fastapi.templating import Jinja2Templates
from lib import  LayoutUtility

templates = Jinja2Templates(directory="resources/templates")

# Load environment variables from .env file
load_dotenv()
DEBUG = os.getenv("DEBUG")

layout = LayoutUtility()






def home_page_controller(request:Request, response:Response):
    
    
    
    
    
    return templates.TemplateResponse("/pages/index.html", {
        "request": request,
        "webpack" :  layout.webpack,
        "DEBUG" : DEBUG,
        "hotreload" : layout.arel.hotreload     
    })