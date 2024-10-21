import os
from dotenv import load_dotenv
from fastapi import Request, Response
from fastapi.templating import Jinja2Templates
from lib import LayoutUtility
templates = Jinja2Templates(directory="resources/templates")


layout = LayoutUtility()


def authenticated_user_page_controller(request:Request, response:Response, id:str):



    
    return templates.TemplateResponse("/pages/authenticated_user_page/authenticated_user_page.html", {
        "request": request,
        "user_id": id,
        "main_css" :  layout.webpack.css,
        "main_bundle_js":  layout.webpack.js
    })