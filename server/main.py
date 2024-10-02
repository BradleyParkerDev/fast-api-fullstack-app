import os
# import arel
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.gzip import GZipMiddleware
from routes import PageRoutes
from routes import UserRoutes


from database.db import init_db
from fastapi.templating import Jinja2Templates
import uvicorn
templates = Jinja2Templates(directory="templates")
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
app.add_middleware(GZipMiddleware)

# Instantiate the PagesRoutes class and include its router
pages_routes = PageRoutes()
app.include_router(pages_routes.setup_routes())

# Instantiate the UserRoutes class and include its router
users_routes = UserRoutes()
app.include_router(users_routes.setup_routes())

# Initialize the database
# init_db()
# print("Database initialized successfully!")

# # Set up hot-reload if DEBUG mode is active
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5001, reload=True)
#     if _debug := os.getenv("DEBUG"):  # Only enable hot-reload in debug mode
#         hot_reload = arel.HotReload(paths=[("static", None), ("templates", None)]) # Watch static and template directories
#         app.add_websocket_route("/hot-reload", route=hot_reload, name="hot-reload")
#         app.add_event_handler("startup", hot_reload.startup)
#         app.add_event_handler("shutdown", hot_reload.shutdown)
#         templates.env.globals["DEBUG"] = _debug
#         templates.env.globals["hot_reload"] = hot_reload


