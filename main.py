from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class App(MDApp):
    def build(self):
        return MDLabel(
            text='Homen aranha',
            halign='center',
            theme_text_color='Custom',
            text_color='white'
        )

App().run()
