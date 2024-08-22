from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.gzip import GZipMiddleware
from livereload import server

app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.mount("/static",StaticFiles(directory="static"), name="static")
app.add_middleware(GZipMiddleware)


@app.get("/")
async def index(request:Request):
    return templates.TemplateResponse("/pages/index.html", {"request":request})
