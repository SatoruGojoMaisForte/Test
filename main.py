
from kivy.animation import Animation
from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivy.properties import StringProperty, ListProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.theming import ThemeManager
from Screens.login_screen.loginscreen import LoginScreen
from Screens.send_code.sendcode import SendCode
from Screens.check_code.checkcode import CheckCode
from Screens.write_code.writecode import WriteCode



class PrincipalApp(MDApp):
    Builder.load_file("screens/login_screen/loginscreen.kv")
    Builder.load_file("screens/send_code/sendcode.kv")
    Builder.load_file("screens/check_code/checkcode.kv")
    Builder.load_file('screens/write_code/writecode.kv')

    def build(self):
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style_switch_animation_duration = 0.8
        Window.size = (400, 700)
        self.screenmanager = ScreenManager()
        self.screenmanager.add_widget(LoginScreen(name="Login"))
        self.screenmanager.add_widget(SendCode(name='Send'))
        self.screenmanager.add_widget(CheckCode(name='Check'))
        self.screenmanager.add_widget(WriteCode(name='Write'))
        return self.screenmanager


PrincipalApp().run()
