import kivy
import time
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.clock import Clock

from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior

#kivy.require("2.0.0")

KV = '''
#:import time time
#:import Clock kivy.clock.Clock
#:import Label kivy.uix.label.Label
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
<Clock_Widget>:
	padding: 10
	time_rn: "Hello"
	MDLabel:
		text: root.time_rn
Screen:
	MDToolbar:
		id: toolbar
		pos_hint: {"top": 1}
		elevation: 8
		title: "Binary Clock"
		left_action_items: [["clock", lambda x: nav_drawer.set_state("open")]]
	NavigationLayout:
		x: toolbar.height
		ScreenManager:
			id: screen_manager
			Screen:
				name: "Settings"
				MDLabel:
					text: "Settings"
			Screen:
				name: "Clock"
				Clock_Widget:
		MDNavigationDrawer:
			id: nav_drawer
			
			ContentNavigationDrawer:
				screen_manager: screen_manager
				nav_drawer: nav_drawer
			
'''
class ContentNavigationDrawer(BoxLayout):
	screen_manager = ObjectProperty()
	nav_drawer = ObjectProperty()
class Clock_Widget(BoxLayout):
	time_rn = StringProperty(time.asctime())
	def __init__(self, **kwargs):
		super(Clock_Widget, self).__init__(**kwargs)
		Clock.schedule_interval(self.update, 1.0 / 60.0)
	def update(self, dt):
		self.time_rn = time.asctime()
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
