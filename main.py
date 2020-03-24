import kivy
import time
from kivy.core.window import Window
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.clock import Clock

from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior

class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class Analog_Widget(BoxLayout):
    def __init__(self, **kwargs):
        super(Analog_Widget, self).__init__(**kwargs)
        Clock.schedule_interval(self.update, 0.5 / 180.0)

    def update(self, dt):
        self.time = time.asctime()
        self.hh0 = f'[b][color=d32f2f]{self.time[11]}[/color][/b]'
        self.hh1 = f'[b][color=ff1744]{self.time[12]}[/color][/b]'
        self.mm0 = f'[b][color=4caf50]{self.time[14]}[/color][/b]'
        self.mm1 = f'[b][color=7cb342]{self.time[15]}[/color][/b]'
        self.ss0 = f'[b][color=2962ff]{self.time[17]}[/color][/b]'
        self.ss1 = f'[b][color=42a5f5]{self.time[18]}[/color][/b]'


class Clock_Widget(BoxLayout):
    time_rn = StringProperty(time.asctime()[11:19])

    def __init__(self, **kwargs):
        super(Clock_Widget, self).__init__(**kwargs)
        Clock.schedule_interval(self.update, 1.0 / 180.0)

    def update(self, dt):
        self.time = time.asctime()
        self.hh0 = f'[b][color=d32f2f]{self.time[11]}[/color][/b]'
        self.h0_ = f'{str(bin(int(self.time[11]))[2::]):>04}'
        self.h0 = f'[b][color=d32f2f]{self.h0_}[/color][/b]'

        if int(self.h0_[0]):
            self.h00 = "[b][color=262626]8[/color][/b]"
        else:
            if clock_app.theme_cls.theme_style == "Dark":
                self.h00 = "[b][color=262626]0[/color][/b]"
            else:
                self.h00 = "[b][color=c0c0c0]0[/color][/b]"
        if int(self.h0_[1]):
            self.h01 = "[b][color=262626]4[/color][/b]"
        else:
            if clock_app.theme_cls.theme_style == "Dark":
                self.h01 = "[b][color=262626]0[/color][/b]"
            else:
                self.h01 = "[b][color=c0c0c0]0[/color][/b]"

        if int(self.h0_[2]):
            self.h02 = f'[b][color=d32f2f]2[/color][/b]'
        else:
            if clock_app.theme_cls.theme_style == "Dark":
                self.h02 = "[b][color=262626]0[/color][/b]"
            else:
                self.h02 = "[b][color=c0c0c0]0[/color][/b]"
        if int(self.h0_[3]):
            self.h03 = f'[b][color=d32f2f]1[/color][/b]'
        else:
            if clock_app.theme_cls.theme_style == "Dark":
                self.h03 = "[b][color=262626]0[/color][/b]"
            else:
                self.h03 = "[b][color=c0c0c0]0[/color][/b]"
        self.hh1 = f'[b][color=ff1744]{self.time[12]}[/color][/b]'
        self.h1_ = f'{str(bin(int(self.time[12]))[2::]):>04}'
        self.h1 = f'[b][color=ff1744]{self.h1_}[/color][/b]'

        if int(self.h1_[0]):
            self.h10 = f'[b][color=ff1744]8[/color][/b]'
        else:
            if clock_app.theme_cls.theme_style == "Dark":
                self.h10 = "[b][color=262626]0[/color][/b]"
            else:
                self.h10 = "[b][color=c0c0c0]0[/color][/b]"
        if int(self.h1_[1]):
            self.h11 = f'[b][color=ff1744]4[/color][/b]'
        else:
            if clock_app.theme_cls.theme_style == "Dark":
                self.h11 = "[b][color=262626]0[/color][/b]"
            else:
                self.h11 = "[b][color=c0c0c0]0[/color][/b]"
        if int(self.h1_[2]):
            self.h12 = f'[b][color=ff1744]2[/color][/b]'
        else:
            if clock_app.theme_cls.theme_style == "Dark":
                self.h12 = "[b][color=262626]0[/color][/b]"
            else:
                self.h12 = "[b][color=c0c0c0]0[/color][/b]"
        if int(self.h1_[3]):
            self.h13 = f'[b][color=ff1744]1[/color][/b]'
        else:
            if clock_app.theme_cls.theme_style == "Dark":
                self.h13 = "[b][color=262626]0[/color][/b]"
            else:
                self.h13 = "[b][color=c0c0c0]0[/color][/b]"
        self.mm0 = f'[b][color=4caf50]{self.time[14]}[/color][/b]'
        self.m0_ = f'{str(bin(int(self.time[14]))[2::]):>04}'
        self.m0 = f'[b][color=4caf50]{self.m0_}[/color][/b]'

        if int(self.m0_[0]):
            self.m00 = "[b][color=262626]8[/color][/b]"
        else:
            if clock_app.theme_cls.theme_style == "Dark":
                self.m00 = "[b][color=262626]0[/color][/b]"
            else:
                self.m00 = "[b][color=c0c0c0]0[/color][/b]"
        if int(self.m0_[1]):
            self.m01 = f'[b][color=4caf50]4[/color][/b]'
        else:
            if clock_app.theme_cls.theme_style == "Dark":
                self.m01 = "[b][color=262626]0[/color][/b]"
            else:
                self.m01 = "[b][color=c0c0c0]0[/color][/b]"
        if int(self.m0_[2]):
            self.m02 = f'[b][color=4caf50]2[/color][/b]'
        else:
            if clock_app.theme_cls.theme_style == "Dark":
                self.m02 = "[b][color=262626]0[/color][/b]"
            else:
                self.m02 = "[b][color=c0c0c0]0[/color][/b]"
        if int(self.m0_[3]):
            self.m03 = f'[b][color=4caf50]1[/color][/b]'
        else:
            if clock_app.theme_cls.theme_style == "Dark":
                self.m03 = "[b][color=262626]0[/color][/b]"
            else:
                self.m03 = "[b][color=c0c0c0]0[/color][/b]"
        self.mm1 = f'[b][color=7cb342]{self.time[15]}[/color][/b]'
        self.m1_ = f'{str(bin(int(self.time[15]))[2::]):>04}'
        self.m1 = f'[b][color=7cb342]{self.m1_}[/color][/b]'

        if int(self.m1_[0]):
            self.m10 = f'[b][color=7cb342]8[/color][/b]'
        else:
            if clock_app.theme_cls.theme_style == "Dark":
                self.m10 = "[b][color=262626]0[/color][/b]"
            else:
                self.m10 = "[b][color=c0c0c0]0[/color][/b]"
        if int(self.m1_[1]):
            self.m11 = f'[b][color=7cb342]4[/color][/b]'
        else:
            if clock_app.theme_cls.theme_style == "Dark":
                self.m11 = "[b][color=262626]0[/color][/b]"
            else:
                self.m11 = "[b][color=c0c0c0]0[/color][/b]"
        if int(self.m1_[2]):
            self.m12 = f'[b][color=7cb342]2[/color][/b]'
        else:
            if clock_app.theme_cls.theme_style == "Dark":
                self.m12 = "[b][color=262626]0[/color][/b]"
            else:
                self.m12 = "[b][color=c0c0c0]0[/color][/b]"
        if int(self.m1_[3]):
            self.m13 = f'[b][color=7cb342]1[/color][/b]'
        else:
            if clock_app.theme_cls.theme_style == "Dark":
                self.m13 = "[b][color=262626]0[/color][/b]"
            else:
                self.m13 = "[b][color=c0c0c0]0[/color][/b]"
        self.ss0 = f'[b][color=2962ff]{self.time[17]}[/color][/b]'
        self.s0_ = f'{str(bin(int(self.time[17]))[2::]):>04}'
        self.s0 = f'[b][color=2962ff]{self.s0_}[/color][/b]'

        if int(self.s0_[0]):
            self.s00 = "[b][color=262626]8[/color][/b]"
        else:
            if clock_app.theme_cls.theme_style == "Dark":
                self.s00 = "[b][color=262626]0[/color][/b]"
            else:
                self.s00 = "[b][color=c0c0c0]0[/color][/b]"
        if int(self.s0_[1]):
            self.s01 = f'[b][color=2962ff]4[/color][/b]'
        else:
            if clock_app.theme_cls.theme_style == "Dark":
                self.s01 = "[b][color=262626]0[/color][/b]"
            else:
                self.s01 = "[b][color=c0c0c0]0[/color][/b]"
        if int(self.s0_[2]):
            self.s02 = f'[b][color=2962ff]2[/color][/b]'
        else:
            if clock_app.theme_cls.theme_style == "Dark":
                self.s02 = "[b][color=262626]0[/color][/b]"
            else:
                self.s02 = "[b][color=c0c0c0]0[/color][/b]"
        if int(self.s0_[3]):
            self.s03 = f'[b][color=2962ff]1[/color][/b]'
        else:
            if clock_app.theme_cls.theme_style == "Dark":
                self.s03 = "[b][color=262626]0[/color][/b]"
            else:
                self.s03 = "[b][color=c0c0c0]0[/color][/b]"
        self.ss1 = f'[b][color=42a5f5]{self.time[18]}[/color][/b]'
        self.s1_ = f'{str(bin(int(self.time[18]))[2::]):>04}'
        self.s1 = f'[b][color=42a5f5]{self.s1_}[/color][/b]'

        if int(self.s1_[0]):
            self.s10 = f'[b][color=42a5f5]8[/color][/b]'
        else:
            if clock_app.theme_cls.theme_style == "Dark":
                self.s10 = "[b][color=262626]0[/color][/b]"
            else:
                self.s10 = "[b][color=c0c0c0]0[/color][/b]"
        if int(self.s1_[1]):
            self.s11 = f'[b][color=42a5f5]4[/color][/b]'
        else:
            if clock_app.theme_cls.theme_style == "Dark":
                self.s11 = "[b][color=262626]0[/color][/b]"
            else:
                self.s11 = "[b][color=c0c0c0]0[/color][/b]"
        if int(self.s1_[2]):
            self.s12 = f'[b][color=42a5f5]2[/color][/b]'
        else:
            if clock_app.theme_cls.theme_style == "Dark":
                self.s12 = "[b][color=262626]0[/color][/b]"
            else:
                self.s12 = "[b][color=c0c0c0]0[/color][/b]"
        if int(self.s1_[3]):
            self.s13 = f'[b][color=42a5f5]1[/color][/b]'
        else:
            if clock_app.theme_cls.theme_style == "Dark":
                self.s13 = "[b][color=262626]0[/color][/b]"
            else:
                self.s13 = "[b][color=c0c0c0]0[/color][/b]"


class ClockApp(MDApp):
    def build(self):
        app = MDApp.get_running_app()
        app.theme_cls.primary_palette = "Gray"
        app.theme_cls.accent_palette = "Gray"
        app.theme_cls.primary_hue = "800"
        app.theme_cls.theme_style = "Dark"
        Window.borderless = False
        self.title = "Tick"
        Config.set('kivy', 'window_title', 'Tick')

    def theme_change(self, instance, value):
        if value:
            clock_app.theme_cls.theme_style = "Light"
            clock_app.theme_cls.primary_palette = "Blue"
            clock_app.theme_cls.accent_palette = "Blue"
            clock_app.theme_cls.primary_hue = "600"
        else:
            clock_app.theme_cls.theme_style = "Dark"
            clock_app.theme_cls.primary_palette = "Gray"
            clock_app.theme_cls.accent_palette = "Gray"
            clock_app.theme_cls.primary_hue = "800"


if __name__ == "__main__":
    clock_app = ClockApp()
    clock_app.run()

