import os
from dotenv import load_dotenv
from fastapi import Request, Response
from fastapi.templating import Jinja2Templates
from lib import  LayoutUtility
templates = Jinja2Templates(directory="resources/templates")

layout = LayoutUtility()

def home_page_controller(request:Request, response:Response):
    
    
    
    
    
    return templates.TemplateResponse("/pages/index.html", {
        "request": request,
        "main_css" :  layout.webpack.css,
        "main_bundle_js":  layout.webpack.js
    })