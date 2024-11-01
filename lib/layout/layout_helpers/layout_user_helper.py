import os
import json
from pathlib import Path
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()
DEBUG = os.getenv("DEBUG")

class LayoutUserHelper:
    
    def __init__(self):
        self.first_name = 'first_name'
        self.last_name = 'last_name'
        self.email_address = 'email_address'
        self.user_name = 'user_name'
        self.user_image = 'user_image'
        
       
