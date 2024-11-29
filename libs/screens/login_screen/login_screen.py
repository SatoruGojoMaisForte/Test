from kivy.network.urlrequest import UrlRequest
from kivy.properties import StringProperty
from kivymd.uix.screen import MDScreen
import bcrypt


class LoginScreen(MDScreen):
    nome = StringProperty()
    perfil = StringProperty()

    def on_enter(self):
        print(self.nome)
        print(self.perfil)
        self.ids.story.avatar = self.perfil
        self.ids.nome.text = self.nome

    def verificar_senha(self):
        url = 'https://obra-7ebd9-default-rtdb.firebaseio.com/Users/.json'
        UrlRequest(
            url,
            method='GET',
            on_success=self.senhas,
        )


    def senhas(self, req, result):
        senha = self.ids.senha.text
        senha_bytes = senha.encode('utf-8')

        for cargo, nome in result.items():
            if nome['name'] == self.nome:
                senha_correta = nome['senha'].encode('utf-8')
                if bcrypt.checkpw(senha_bytes, senha_correta):
                    self.ids.senha.error = False
                    self.ids.senha_correta.text = ''
                    print('senha correta meu nobre')
                else:
                    print('senha está errada seu acefalo burro do caralho')
                    self.ids.senha.error = True
                    self.ids.senha_correta.text = 'A senha inserida está incorreta'
                break
