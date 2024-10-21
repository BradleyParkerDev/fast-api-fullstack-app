from fastapi import Request, Response
from fastapi.templating import Jinja2Templates
from lib import LayoutUtility
templates = Jinja2Templates(directory="resources/templates")


layout = LayoutUtility()


def user_page_controller(request:Request, response:Response):



    return templates.TemplateResponse("/pages/user_page/user_page.html", {
        "request": request,
        "main_css" :  layout.webpack.css,
        "main_bundle_js":  layout.webpack.js
    })