import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout

kivy.require("2.0.0")


class ClockApp(App):
    def build(self):
        app = App.get_running_app()
        self.grid_layout = GridLayout()
        return self.grid_layout

if __name__ == "__main__":
    clock_app = ClockApp()
    clock_app.run()