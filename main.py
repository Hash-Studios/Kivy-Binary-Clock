import kivy
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty

from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior

#kivy.require("2.0.0")

KV = '''
<ContentNavigationDrawer>:
	ScrollView:
		MDList:
		    OneLineListItem:
		        text: "Binary Clock"
		        on_press:
		            root.nav_drawer.set_state("close")
		            root.screen_manager.current = "Clock"
		    OneLineListItem:
		        text: "Settings"
		        on_press:
		            root.nav_drawer.set_state("close")
		            root.screen_manager.current = "Settings"

Screen:
	MDToolbar:
		id: toolbar
		pos_hint: {"top": 1}
		elevation: 8
		title: "Binary Clock"
		left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
	NavigationLayout:
		x: toolbar.height
		ScreenManager:
			id: screen_manager
			Screen:
				name: "Clock"
				GridLayout:
					cols: 6
					MDLabel:
						text: "H"
					MDLabel:
						text: "H"
					MDLabel:
						text: "M"
					MDLabel:
						text: "M"
					MDLabel:
						text: "S"
					MDLabel:
						text: "S"
			Screen:
				name: "Settings"
				Label:
					text: "Settings"
		MDNavigationDrawer:
			id: nav_drawer
			
			ContentNavigationDrawer:
				screen_manager: screen_manager
				nav_drawer: nav_drawer
			
'''
class ContentNavigationDrawer(BoxLayout):
	screen_manager = ObjectProperty()
	nav_drawer = ObjectProperty()

class ClockApp(MDApp):
    def build(self):
        app = MDApp.get_running_app()
        app.theme_cls.primary_palette = "Amber"
        app.theme_cls.accent_palette = "Amber"
        app.theme_cls.theme_style = "Dark"
        Window.borderless = False
        self.title = "Binary Clock"
        Config.set('kivy', 'window_title', 'Binary Clock')
        return Builder.load_string(KV)


if __name__ == "__main__":
    clock_app = ClockApp()
    clock_app.run()
