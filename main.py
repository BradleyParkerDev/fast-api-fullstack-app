from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.gzip import GZipMiddleware
from routes.pages.PageRoutes import PagesRoutes
from routes.users.UserRoutes import UserRoutes
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
app.add_middleware(GZipMiddleware)

# Instantiate the PagesRoutes class and include its router
pages_routes = PagesRoutes()
app.include_router(pages_routes.setup_routes())

users_routes = UserRoutes()
app.include_router(users_routes.setup_routes())

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=5001)

