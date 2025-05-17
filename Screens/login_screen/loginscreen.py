from kivymd.uix.dialog import MDDialog, MDDialogHeadlineText, MDDialogButtonContainer, MDDialogSupportingText
from screens.send_code.sendcode import SendCode
from kivymd.uix.button import MDButton, MDButtonText
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivymd.uix.screen import MDScreen
from kivymd.uix.widget import MDWidget
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
import requests

click_button_user = 0
click_button_password = 0
word = 0


class LoginScreen(MDScreen):
    def theme(self):
        if self.theme_cls.theme_style == "Dark":
            self.theme_cls.theme_style = "Light"
        else:
            self.theme_cls.theme_style = "Dark"

    def check_name(self):
        name = self.ids.usuario.text

        # Check if the name exists in the database
        response = requests.get(f"https://apis-chatto.onrender.com/check-name?name={name}")
        data = response.json()

        if data['exists']:
             return True
        else:
             return False

    def check_password(self, name, password):
        url = f"https://apis-chatto.onrender.com/check-password?name={name}&password={password}"
        response = requests.get(url)
        data = response.json()
        if not data['exists']:
            return False
        else:
            return True

    def focus(self):
        global click_button_user, click_button_password
        textfield_usuario = self.ids.usuario
        textfield_password = self.ids.senha
        text_user = self.ids.usuario.text
        text_password = textfield_password.text
        # verificações se os campos estiverem vazios.
        if not textfield_usuario.focus and not textfield_usuario.text:
            textfield_usuario.focus = True
            click_button_user += 1

        if text_user:
            textfield_password.focus = True

        if text_user and text_password:
            user_existir = self.check_name()

            if not user_existir:
                self.ids.encontrar.text = 'Usuario não cadastrado'
                self.ids.usuario.error = True

            else:
                self.ids.encontrar.text = ''
                senha = self.check_password(self.ids.usuario.text, self.ids.senha.text)

                if senha == True:
                    self.ids.senha_correta.text = ''
                else:
                    self.ids.senha_correta.text = 'A senha está incorreta'
                    self.ids.senha.error = True

    def chamar_trocar(self, *args):
        self.manager.current = "Send"
