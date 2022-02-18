from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

Builder.load_string('''
<OneScreen>
    Label:
        text: app.saying
''')

class OneScreen(Screen):
    pass

class TestApp(App):
    def __init__(self, **kwargs):
        self.saying = 'I was read from app instance.'
        super(TestApp, self).__init__(**kwargs)

    def build(self):
        return OneScreen()

TestApp().run()