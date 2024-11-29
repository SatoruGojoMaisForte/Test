import json

import bcrypt
from kivy.network.urlrequest import UrlRequest
from kivy.uix.screenmanager import SlideTransition
from kivymd.uix.screen import MDScreen


class RegisterScreen(MDScreen):
    def verificar(self):
        self.verificar_nome()
        if self.ids.name.text == '':
            self.ids.name.focus = True
            return

        if self.ids.name.text != '' and self.ids.password.text == '':
            self.ids.password.focus = True
            return



    def verificar_nome(self):
        url = 'https://obra-7ebd9-default-rtdb.firebaseio.com/Users/.json'
        UrlRequest(
            url,
            method='GET',
            on_success=self.nomes,
        )
    def nomes(self, req, result):
        for cargo, nome in result.items():
            if nome['name'] == self.ids.name.text:
                self.ids.name.error = True
                self.ids.h1.text = 'O nome já possui um usuario cadastrado'
                break
            else:
                self.ids.name.error = False
                self.ids.h1.text = ''
                self.cadastrar()
                break

    def cadastrar(self):
        url = 'https://obra-7ebd9-default-rtdb.firebaseio.com/Users'
        hashed_password = self.ids.password.text.encode('utf-8')
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password=hashed_password, salt=salt).decode('utf-8')
        data = {"name": self.ids.name.text, 'senha': hashed_password, 'perfil': 'https://res.cloudinary.com/dsmgwupky/image/upload/v1731366361/image_o6cbgf.png'}
        UrlRequest(
            f'{url}/.json',
            method='POST',
            on_success=self.cadastrado,
            req_body=json.dumps(data),
            req_headers={'Content-Type': 'application/json'}
        )

    def cadastrado(self, req, result):
        self.init()

    def init(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'Init'

