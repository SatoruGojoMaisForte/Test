import re
import requests
from kivy.properties import StringProperty
from kivymd.uix.screen import MDScreen
from dotenv import set_key, dotenv_values


class SendCode(MDScreen):

    def save_email_to_env(self, email):
        env_file = ".env"
        set_key(env_file, "EMAIL_USER", email)

    def set_email(self):
        self.verificar_email = self.ids.verificar_email.text

    def chama_login(self):
        self.manager.current = 'Login'

    def is_email_valid(self, text: str) -> bool:
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, text) is not None

    def email_existir(self, email):
        email_enviar = email

        # Check if the name exists in the database
        response = requests.get(f"https://apis-chatto.onrender.com/check-email?email={email_enviar}")
        data = response.json()

        if data['existir']:
             return True
        else:
             return False

    def send_verification_email(self, email):
        response = requests.post(f"https://apis-chatto.onrender.com/send_verification_code?email={email}")
        data = response.json()

        if data['enviado']:
            return True

        else:
            return False

    def enviar_codigo(self):
        # verificar se ele está vazio
        texto = self.ids.verificar_email.text

        if texto:
            # verificar se o texto está no formato de um email
            if self.is_email_valid(texto):
                self.ids.erros.text = ''
                email_existi = self.email_existir(texto)

                if email_existi:
                    # enviar um codigo de verificação no email da pessoa
                    enviar = self.send_verification_email(texto)
                    if enviar:
                        self.manager.current = ("Check")
                        self.save_email_to_env(email=texto)
                    else:
                        print('Falha ao enviar')

            if not self.is_email_valid(texto):
                self.ids.verificar_email.error = True
                self.ids.erros.text = 'O email está em um formato invalido'
        else:
            self.ids.verificar_email.error = True
            self.ids.erros.text = 'Preencha o campo com o email'


