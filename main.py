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
	h1: ""
	h2: ""
	m1: ""
	m2: ""
	s1: ""
	s2: ""
	GridLayout:
		cols: 6
		MDLabel:
			text: "H"
			halign: "center"
			valign: "middle"
			theme_text_color: "Primary"
			font_style: "H2"
		MDLabel:
			text: "H"
			halign: "center"
			valign: "middle"
			theme_text_color: "Primary"
			font_style: "H2"
		MDLabel:
			text: "M"
			halign: "center"
			valign: "middle"
			theme_text_color: "Primary"
			font_style: "H2"
		MDLabel:
			text: "M"
			halign: "center"
			valign: "middle"
			theme_text_color: "Primary"
			font_style: "H2"
		MDLabel:
			text: "S"
			halign: "center"
			valign: "middle"
			theme_text_color: "Primary"
			font_style: "H2"
		MDLabel:
			text: "S"
			halign: "center"
			valign: "middle"
			theme_text_color: "Primary"
			font_style: "H2"
		MDLabel:
			text: root.h1
			halign: "center"
			valign: "middle"
			theme_text_color: "Primary"
			font_style: "H4"
		MDLabel:
			text: root.h2
			halign: "center"
			valign: "middle"
			theme_text_color: "Primary"
			font_style: "H4"
		MDLabel:
			text: root.m1
			halign: "center"
			valign: "middle"
			theme_text_color: "Primary"
			font_style: "H4"
		MDLabel:
			text: root.m2
			halign: "center"
			valign: "middle"
			theme_text_color: "Primary"
			font_style: "H4"
		MDLabel:
			text: root.s1
			halign: "center"
			valign: "middle"
			theme_text_color: "Primary"
			font_style: "H4"
		MDLabel:
			text: root.s2
			halign: "center"
			valign: "middle"
			theme_text_color: "Primary"
			font_style: "H4"
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
				name: "Clock"
				Clock_Widget:
			Screen:
				name: "Settings"
				MDLabel:
					text: "Settings"
					halign: "center"
					valign: "middle"
					theme_text_color: "Primary"
					font_style: "H1"
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
	time_rn = StringProperty(time.asctime()[11:19])
	def __init__(self, **kwargs):
		super(Clock_Widget, self).__init__(**kwargs)
		Clock.schedule_interval(self.update, 1.0 / 180.0)
	def update(self, dt):
		self.time = time.asctime()
		self.h1 = f'{str(bin(int(self.time[11]))[2::]):>04}'
		self.h2 = f'{str(bin(int(self.time[12]))[2::]):>04}'
		self.m1 = f'{str(bin(int(self.time[14]))[2::]):>04}'
		self.m2 = f'{str(bin(int(self.time[15]))[2::]):>04}'
		self.s1 = f'{str(bin(int(self.time[17]))[2::]):>04}'
		self.s2 = f'{str(bin(int(self.time[18]))[2::]):>04}'
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
