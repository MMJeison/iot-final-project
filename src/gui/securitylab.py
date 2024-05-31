from kivymd.app import MDApp
from kivy.lang import Builder

class MainGUIApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_file('src/gui/securitylab.kv')
