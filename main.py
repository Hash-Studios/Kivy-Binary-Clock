import kivy
from kivymd.app import MDApp
from kivy.uix.gridlayout import GridLayout

kivy.require("2.0.0")


class ClockApp(MDApp):
    def build(self):
        app = MDApp.get_running_app()
        self.grid_layout = GridLayout()
        return self.grid_layout


if __name__ == "__main__":
    clock_app = ClockApp()
    clock_app.run()
