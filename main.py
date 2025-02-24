from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivymd.uix.screenmanager import MDScreenManager
from screens.test_screen.test_screen import Test


class Main(MDApp):
    def build(self):
        Window.size = (350, 700)
        self.load_all_kv_files()
        self.screenmanager = MDScreenManager()
        self.screenmanager.add_widget(Test(name='test'))
        return self.screenmanager

    def load_all_kv_files(self):
        Builder.load_file('screens/test_screen/test_screen.kv')
        

Main().run()

