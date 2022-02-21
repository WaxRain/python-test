import re
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.properties import NumericProperty, ListProperty
from kivy.config import Config

Config.set('kivy', 'default_font', ["KAI", "data/fonts/STKAITI.TTF"])
Config.set("graphics", "width", 600)
Config.set("graphics", "height", 600)
Config.set("graphics", "resizable", 0)

class FloatInput(TextInput):

    pat = re.compile('[^0-9]')
    def insert_text(self, substring, from_undo=False):
        pat = self.pat
        if '.' in self.text:
            s = re.sub(pat, '', substring)
        else:
            s = '.'.join([re.sub(pat, '', s) for s in substring.split('.', 1)])
        return super(FloatInput, self).insert_text(s, from_undo=from_undo)


class Sensitivity(GridLayout):
    FPR = NumericProperty(0)
    FNR = NumericProperty(0)
    PPV = NumericProperty(0)
    NPV = NumericProperty(0)
    pass


class SensitivityApp(App):
    def build(self):
        return Sensitivity()

    def process(self):
         text = self.root.ids.PPV.text = 1003
         print (text)


if __name__ == "__main__":
    SensitivityApp().run()