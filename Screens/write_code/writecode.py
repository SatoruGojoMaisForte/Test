import os
import requests
from kivymd.uix.screen import MDScreen
from dotenv import load_dotenv
from time import sleep
load_dotenv()


class WriteCode(MDScreen):

    def check_code(self):
        code = self.ids.codigo.text
        email = os.getenv('EMAIL_USER')
        print(f'{email}')
        response = requests.post(f"https://apis-chatto.onrender.com/verify_code?email={os.getenv('EMAIL_USER')}&code={code}")
        data = response.json()
        if data['message'] == 'O codigo digitado está correto':
            return True

        elif data['message'] == 'O codigo digitado está expirado':
            return False

    def check_text_length(self):
        text_field = self.ids.codigo
        max_length = 6

        # Remove existing spaces and limit the length to max_length
        text = text_field.text.replace(' ', '')
        if len(text) > max_length:
            text = text[:max_length]

        # Format the text in groups of 3 characters
        formatted_text = ''.join(''.join(text[i:i + 3]) for i in range(0, len(text), 3))

        # Disable on_text event temporarily to avoid infinite loop
        text_field.text = formatted_text
        text_field.halign = 'center'
        text_field.font_size = 40

    def check(self):
        check = self.check_code()
        self.manager.current = 'Progress'
        print('so testado {}'.format(check))


