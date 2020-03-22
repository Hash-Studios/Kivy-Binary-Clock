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
			markup: True
			halign: "center"
			valign: "middle"
			theme_text_color: "Secondary"
			font_style: "H4"
		MDLabel:
			text: root.h10
			markup: True
			halign: "center"
			valign: "middle"
			theme_text_color: "Secondary"
			font_style: "H4"
		MDLabel:
			text: root.m00
			markup: True
			halign: "center"
			valign: "middle"
			theme_text_color: "Secondary"
			font_style: "H4"
		MDLabel:
			text: root.m10
			markup: True
			halign: "center"
			valign: "middle"
			theme_text_color: "Secondary"
			font_style: "H4"
		MDLabel:
			text: root.s00
			markup: True
			halign: "center"
			valign: "middle"
			theme_text_color: "Secondary"
			font_style: "H4"
		MDLabel:
			text: root.s10
			markup: True
			halign: "center"
			valign: "middle"
			theme_text_color: "Secondary"
			font_style: "H4"
		
		
		
		MDLabel:
			text: root.h01
			markup: True
			halign: "center"
			valign: "middle"
			theme_text_color: "Secondary"
			font_style: "H4"
		MDLabel:
			text: root.h11
			markup: True
			halign: "center"
			valign: "middle"
			theme_text_color: "Secondary"
			font_style: "H4"
		MDLabel:
			text: root.m01
			markup: True
			halign: "center"
			valign: "middle"
			theme_text_color: "Secondary"
			font_style: "H4"
		MDLabel:
			text: root.m11
			markup: True
			halign: "center"
			valign: "middle"
			theme_text_color: "Secondary"
			font_style: "H4"
		MDLabel:
			text: root.s01
			markup: True
			halign: "center"
			valign: "middle"
			theme_text_color: "Secondary"
			font_style: "H4"
		MDLabel:
			text: root.s11
			markup: True
			halign: "center"
			valign: "middle"
			theme_text_color: "Secondary"
			font_style: "H4"
		
		
		
		
		MDLabel:
			text: root.h02
			markup: True
			halign: "center"
			valign: "middle"
			theme_text_color: "Secondary"
			font_style: "H4"
		MDLabel:
			text: root.h12
			markup: True
			halign: "center"
			valign: "middle"
			theme_text_color: "Secondary"
			font_style: "H4"
		MDLabel:
			text: root.m02
			markup: True
			halign: "center"
			valign: "middle"
			theme_text_color: "Secondary"
			font_style: "H4"
		MDLabel:
			text: root.m12
			markup: True
			halign: "center"
			valign: "middle"
			theme_text_color: "Secondary"
			font_style: "H4"
		MDLabel:
			text: root.s02
			markup: True
			halign: "center"
			valign: "middle"
			theme_text_color: "Secondary"
			font_style: "H4"
		MDLabel:
			text: root.s12
			markup: True
			halign: "center"
			valign: "middle"
			theme_text_color: "Secondary"
			font_style: "H4"
			
		
		
		
		MDLabel:
			text: root.h03
			markup: True
			halign: "center"
			valign: "middle"
			theme_text_color: "Secondary"
			font_style: "H4"
		MDLabel:
			text: root.h13
			markup: True
			halign: "center"
			valign: "middle"
			theme_text_color: "Secondary"
			font_style: "H4"
		MDLabel:
			text: root.m03
			markup: True
			halign: "center"
			valign: "middle"
			theme_text_color: "Secondary"
			font_style: "H4"
		MDLabel:
			text: root.m13
			markup: True
			halign: "center"
			valign: "middle"
			theme_text_color: "Secondary"
			font_style: "H4"
		MDLabel:
			text: root.s03
			markup: True
			halign: "center"
			valign: "middle"
			theme_text_color: "Secondary"
			font_style: "H4"
		MDLabel:
			text: root.s13
			markup: True
			halign: "center"
			valign: "middle"
			theme_text_color: "Secondary"
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
				GridLayout:
					padding: 5
					cols: 1
					MDLabel:
					MDLabel:
						text: "Settings"
						halign: "center"
						valign: "middle"
						theme_text_color: "Primary"
						font_style: "H2"
					GridLayout:
						cols: 2
						MDLabel:
							text: "Dark Mode"
							halign: "center"
							valign: "middle"
							theme_text_color: "Primary"
							font_style: "Body1"
						FloatLayout:
							MDSwitch:
								pos_hint: {'center_x': .5, 'center_y': .5}
								active: False
								on_active: app.theme_change(self, self.active)
					MDLabel:
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
		
		
		if int(self.h0[0]):
			self.h00 = f' '
		else:
			self.h00 = " "
		if int(self.h0[1]):
			self.h01 = f' '
		else:
			self.h01 = " "
		if int(self.h0[2]):
			self.h02 = f'[color=ffbf00]1[/color]'
		else:
			self.h02 = "X"
		if int(self.h0[3]):
			self.h03 = f'[color=ffbf00]1[/color]'
		else:
			self.h03 = "X"
			
			
		self.h1 = f'{str(bin(int(self.time[12]))[2::]):>04}'
		
		
		if int(self.h1[0]):
			self.h10 = f'[color=ffbf00]1[/color]'
		else:
			self.h10 = "X"
		if int(self.h1[1]):
			self.h11 = f'[color=ffbf00]1[/color]'
		else:
			self.h11 = "X"
		if int(self.h1[2]):
			self.h12 = f'[color=ffbf00]1[/color]'
		else:
			self.h12 = "X"
		if int(self.h1[3]):
			self.h13 = f'[color=ffbf00]1[/color]'
		else:
			self.h13 = "X"
			
			
		self.m0 = f'{str(bin(int(self.time[14]))[2::]):>04}'
		
		
		if int(self.m0[0]):
			self.m00 = f' '
		else:
			self.m00 = " "
		if int(self.m0[1]):
			self.m01 = f'[color=ffbf00]1[/color]'
		else:
			self.m01 = "X"
		if int(self.m0[2]):
			self.m02 = f'[color=ffbf00]1[/color]'
		else:
			self.m02 = "X"
		if int(self.m0[3]):
			self.m03 = f'[color=ffbf00]1[/color]'
		else:
			self.m03 = "X"
			
			
		self.m1 = f'{str(bin(int(self.time[15]))[2::]):>04}'
		
		
		if int(self.m1[0]):
			self.m10 = f'[color=ffbf00]1[/color]'
		else:
			self.m10 = "X"
		if int(self.m1[1]):
			self.m11 = f'[color=ffbf00]1[/color]'
		else:
			self.m11 = "X"
		if int(self.m1[2]):
			self.m12 = f'[color=ffbf00]1[/color]'
		else:
			self.m12 = "X"
		if int(self.m1[3]):
			self.m13 = f'[color=ffbf00]1[/color]'
		else:
			self.m13 = "X"
			
			
		self.s0 = f'{str(bin(int(self.time[17]))[2::]):>04}'
		
		
		if int(self.s0[0]):
			self.s00 = f' '
		else:
			self.s00 = " "
		if int(self.s0[1]):
			self.s01 = f'[color=ffbf00]1[/color]'
		else:
			self.s01 = "X"
		if int(self.s0[2]):
			self.s02 = f'[color=ffbf00]1[/color]'
		else:
			self.s02 = "X"
		if int(self.s0[3]):
			self.s03 = f'[color=ffbf00]1[/color]'
		else:
			self.s03 = "X"
			
			
		self.s1 = f'{str(bin(int(self.time[18]))[2::]):>04}'
		
		
		if int(self.s1[0]):
			self.s10 = f'[color=ffbf00]1[/color]'
		else:
			self.s10 = "X"
		if int(self.s1[1]):
			self.s11 = f'[color=ffbf00]1[/color]'
		else:
			self.s11 = "X"
		if int(self.s1[2]):
			self.s12 = f'[color=ffbf00]1[/color]'
		else:
			self.s12 = "X"
		if int(self.s1[3]):
			self.s13 = f'[color=ffbf00]1[/color]'
		else:
			self.s13 = "X"
			
			
class ClockApp(MDApp):
    def build(self):
        app = MDApp.get_running_app()
        app.theme_cls.primary_palette = "Amber"
        app.theme_cls.accent_palette = "Amber"
        app.theme_cls.theme_style = "Light"
        Window.borderless = False
        self.title = "Binary Clock"
        Config.set('kivy', 'window_title', 'Binary Clock')
        return Builder.load_string(KV)
    def theme_change(self, instance, value):
    	if value:
    		clock_app.theme_cls.theme_style = "Dark"
    	else:
    		clock_app.theme_cls.theme_style = "Light"


if __name__ == "__main__":
    clock_app = ClockApp()
    clock_app.run()
