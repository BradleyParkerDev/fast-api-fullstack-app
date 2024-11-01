from lib import LayoutWebpackHelper, LayoutArelHelper, LayoutUserHelper

class LayoutUtility:
    
    def __init__(self):
        # app_name could appear in the logo for the templates
        self.user = LayoutUserHelper()
        self.webpack = LayoutWebpackHelper()
        self.arel = LayoutArelHelper()

        
    def set_user_theme(self, theme):
        
        return theme