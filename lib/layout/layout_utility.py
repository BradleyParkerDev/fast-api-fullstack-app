from lib import LayoutWebpackHelper, LayoutArelHelper

class LayoutUtility:
    
    def __init__(self):
        self.app_name = "FastAPI App"
        self.webpack = LayoutWebpackHelper()
        self.arel = LayoutArelHelper()

        
    def set_user_theme(self, theme):
        
        return theme