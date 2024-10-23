import os
import json
from pathlib import Path
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()
DEBUG = os.getenv("DEBUG")

class LayoutWebpackHelper:
    def __init__(self):
        self.webpack_port = os.getenv("WEBPACK_PORT")
        self.fastapi_port = os.getenv("FASTAPI_PORT")
        self.manifest = {}
        
        if DEBUG == 'true':
            # Development mode
            self.css = f"http://localhost:{self.webpack_port}/css/main.css"
            self.js = f"http://localhost:{self.webpack_port}/js/main.bundle.js"
            self.home_page_js = f"http://localhost:{self.webpack_port}/js/homePage.bundle.js"
            self.user_page_js = f"http://localhost:{self.webpack_port}/js/userPage.bundle.js"
            self.authenticated_userpage_js = f"http://localhost:{self.webpack_port}/js/authenticateUserPage.bundle.js"
        else:
            # Production: load manifest.json
            manifest_path = Path("public/build/manifest.json")
            if manifest_path.exists():
                with open(manifest_path, "r") as f:
                    self.manifest = json.load(f)
                self.css = self.manifest.get("main.css", f"http://localhost:{self.webpack_port}/css/main.css")
                self.js = self.manifest.get("main.js", f"http://localhost:{self.webpack_port}/js/main.bundle.js")
                self.home_page_js = self.manifest.get("homePage.js",f"http://localhost:{self.webpack_port}/js/homePage.bundle.js")
                self.user_page_js = self.manifest.get("userPage.js",f"http://localhost:{self.webpack_port}/js/userPage.bundle.js")
                self.authenticated_userpage_js = self.manifest.get("authenticatedUserPage.js",f"http://localhost:{self.webpack_port}/js/authenticateUserPage.bundle.js")
            else:
                # Fallback if manifest.json does not exist
                self.css = f"http://localhost:{self.webpack_port}/css/main.css"
                self.js = f"http://localhost:{self.webpack_port}/js/main.bundle.js"
                self.home_page_js = f"http://localhost:{self.webpack_port}/js/homePage.bundle.js"
                self.user_page_js = f"http://localhost:{self.webpack_port}/js/userPage.bundle.js"
                self.authenticated_userpage_js = f"http://localhost:{self.webpack_port}/js/authenticateUserPage.bundle.js"
