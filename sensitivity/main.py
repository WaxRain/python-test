from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config

Config.set('kivy', 'default_font', ["KAI", "data/fonts/STKAITI.TTF"])
Config.set("graphics", "width", 600)
Config.set("graphics", "height", 600)
Config.set("graphics", "resizable", 0)


class Sensitivity(GridLayout):
    pass


class SensitivityApp(App):
    def build(self):
        return Sensitivity()


if __name__ == "__main__":
    SensitivityApp().run()