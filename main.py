import kivy
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior

kivy.require("2.0.0")

KV = '''
#:import NavigationDrawerToolbar kivymd.navigationdrawer.NavigationDrawerToolbar
NavigationLayout:
    MDNavigationDrawer:
        drawer_logo: "C:/User/Asus/Desktop/Kivy-Chat-App/icon.png"
        spacing: 8
        NavigationDrawerToolbar:
            elevation: 8
            title: "Binary Clock"
'''


class ClockApp(MDApp):
    def build(self):
        app = MDApp.get_running_app()
        app.theme_cls.primary_palette = "DeepOrange"
        app.theme_cls.accent_palette = "DeepOrange"
        app.theme_cls.theme_style = "Dark"
        Window.size = (640, 360)
        Window.borderless = False
        self.title = "Binary Clock"
        Config.set('kivy', 'window_title', 'Binary Clock')
        return Builder.load_string(KV)


if __name__ == "__main__":
    clock_app = ClockApp()
    clock_app.run()
