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
	padding: 5
	h00: ""
	h01: ""
	h02: ""
	h03: ""
	h10: ""
	h11: ""
	h12: ""
	h13: ""
	m00: ""
	m01: ""
	m02: ""
	m03: ""
	m10: ""
	m11: ""
	m12: ""
	m13: ""
	s00: ""
	s01: ""
	s02: ""
	s03: ""
	s10: ""
	s11: ""
	s12: ""
	s13: ""
	GridLayout:
		padding: 40
		cols: 6
		
		
		MDLabel:
		MDLabel:
		MDLabel:
		MDLabel:
		MDLabel:
		MDLabel:
		
		
		
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
			text: root.h00
			halign: "center"
			valign: "middle"
			theme_text_color: "Primary"
			font_style: "H4"
		MDLabel:
			text: root.h10
			halign: "center"
			valign: "middle"
			theme_text_color: "Primary"
			font_style: "H4"
		MDLabel:
			text: root.m00
			halign: "center"
			valign: "middle"
			theme_text_color: "Primary"
			font_style: "H4"
		MDLabel:
			text: root.m10
			halign: "center"
			valign: "middle"
			theme_text_color: "Primary"
			font_style: "H4"
		MDLabel:
			text: root.s00
			halign: "center"
			valign: "middle"
			theme_text_color: "Primary"
			font_style: "H4"
		MDLabel:
			text: root.s10
			halign: "center"
			valign: "middle"
			theme_text_color: "Primary"
			font_style: "H4"
		
		
		
		MDLabel:
			text: root.h01
			halign: "center"
			valign: "middle"
			theme_text_color: "Primary"
			font_style: "H4"
		MDLabel:
			text: root.h11
			halign: "center"
			valign: "middle"
			theme_text_color: "Primary"
			font_style: "H4"
		MDLabel:
			text: root.m01
			halign: "center"
			valign: "middle"
			theme_text_color: "Primary"
			font_style: "H4"
		MDLabel:
			text: root.m11
			halign: "center"
			valign: "middle"
			theme_text_color: "Primary"
			font_style: "H4"
		MDLabel:
			text: root.s01
			halign: "center"
			valign: "middle"
			theme_text_color: "Primary"
			font_style: "H4"
		MDLabel:
			text: root.s11
			halign: "center"
			valign: "middle"
			theme_text_color: "Primary"
			font_style: "H4"
		
		
		
		
		MDLabel:
			text: root.h02
			halign: "center"
			valign: "middle"
			theme_text_color: "Primary"
			font_style: "H4"
		MDLabel:
			text: root.h12
			halign: "center"
			valign: "middle"
			theme_text_color: "Primary"
			font_style: "H4"
		MDLabel:
			text: root.m02
			halign: "center"
			valign: "middle"
			theme_text_color: "Primary"
			font_style: "H4"
		MDLabel:
			text: root.m12
			halign: "center"
			valign: "middle"
			theme_text_color: "Primary"
			font_style: "H4"
		MDLabel:
			text: root.s02
			halign: "center"
			valign: "middle"
			theme_text_color: "Primary"
			font_style: "H4"
		MDLabel:
			text: root.s12
			halign: "center"
			valign: "middle"
			theme_text_color: "Primary"
			font_style: "H4"
			
		
		
		
		MDLabel:
			text: root.h03
			halign: "center"
			valign: "middle"
			theme_text_color: "Primary"
			font_style: "H4"
		MDLabel:
			text: root.h13
			halign: "center"
			valign: "middle"
			theme_text_color: "Primary"
			font_style: "H4"
		MDLabel:
			text: root.m03
			halign: "center"
			valign: "middle"
			theme_text_color: "Primary"
			font_style: "H4"
		MDLabel:
			text: root.m13
			halign: "center"
			valign: "middle"
			theme_text_color: "Primary"
			font_style: "H4"
		MDLabel:
			text: root.s03
			halign: "center"
			valign: "middle"
			theme_text_color: "Primary"
			font_style: "H4"
		MDLabel:
			text: root.s13
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
		self.h0 = f'{str(bin(int(self.time[11]))[2::]):>04}'
		self.h00 = self.h0[0]
		self.h01 = self.h0[1]
		self.h02 = self.h0[2]
		self.h03 = self.h0[3]
		self.h1 = f'{str(bin(int(self.time[12]))[2::]):>04}'
		self.h10 = self.h1[0]
		self.h11 = self.h1[1]
		self.h12 = self.h1[2]
		self.h13 = self.h1[3]
		self.m0 = f'{str(bin(int(self.time[14]))[2::]):>04}'
		self.m00 = self.m0[0]
		self.m01 = self.m0[1]
		self.m02 = self.m0[2]
		self.m03 = self.m0[3]
		self.m1 = f'{str(bin(int(self.time[15]))[2::]):>04}'
		self.m10 = self.m1[0]
		self.m11 = self.m1[1]
		self.m12 = self.m1[2]
		self.m13 = self.m1[3]
		self.s0 = f'{str(bin(int(self.time[17]))[2::]):>04}'
		self.s00 = self.s0[0]
		self.s01 = self.s0[1]
		self.s02 = self.s0[2]
		self.s03 = self.s0[3]
		self.s1 = f'{str(bin(int(self.time[18]))[2::]):>04}'
		self.s10 = self.s1[0]
		self.s11 = self.s1[1]
		self.s12 = self.s1[2]
		self.s13 = self.s1[3]
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
