from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen


kv = Builder.load_string("""
<OneScreen>:
    Label:
        font_size: 70
        text: "my mother screen was created "
""")

class OneScreen(Screen):
    pass


class TestApp(App):
    def build(self):
        return kv

TestApp().run()