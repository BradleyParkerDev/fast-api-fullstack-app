from lib import LayoutWebpackHelper, LayoutArelHelper

class LayoutUtility:
    
    def __init__(self):
        self.webpack = LayoutWebpackHelper()
        self.arel = LayoutArelHelper()

        
    def set_user_theme(self, theme):
        
        return theme