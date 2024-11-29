import json

from kivy.network.urlrequest import UrlRequest
from kivy.properties import StringProperty
from kivy.uix.image import AsyncImage
from kivymd.uix.button import MDIconButton
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.progressindicator import MDCircularProgressIndicator
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.screen import MDScreen


class StepFour(MDScreen):
    contratante = StringProperty()
    nome = StringProperty()
    cpf = StringProperty()
    pix =StringProperty()
    contratado = StringProperty()
    idade = StringProperty()
    competencias = StringProperty()
    cargo = StringProperty()

    def on_enter(self, *args):
        print(self.contratante, self.nome, self.cpf, self.pix, self.contratado, self.idade, self.competencias, self.cargo)
        # Definindo o ícone de erro para as telas
        icone_erro = MDIconButton(
            icon='alert-circle',
            theme_font_size='Custom',
            font_size='55sp',
            theme_icon_color='Custom',
            pos_hint={'center_x': .5, 'center_y': .6},
            icon_color='red'  # Cor vermelha para representar o erro
        )
        self.ids['error'] = icone_erro

        # Definindo o ícone de acerto para as telas
        icone_acerto = AsyncImage(
            source='https://res.cloudinary.com/dsmgwupky/image/upload/v1730504140/image_yvn8lp.png',
            size_hint=(None, None),
            size=("80dp", "150dp"),
            pos_hint={"center_x": 0.5, "center_y": 0.65},
            allow_stretch=True
        )
        self.ids['acerto'] = icone_acerto

        # Definindo o MDCard onde vai ficar todo o corpo do layout
        self.card = MDCard(
            id='carregando',
            style='elevated',
            size_hint=(1, 1),
            pos_hint={"center_y": 0.5, "center_x": 0.5},
            padding="16dp",
            md_bg_color=(1, 1, 1, 1),
            theme_bg_color="Custom",
            theme_shadow_offset="Custom",
            shadow_offset=(1, -2),
            theme_shadow_softness="Custom",
            shadow_softness=1,
            theme_elevation_level="Custom",
            elevation_level=2
        )
        self.ids['card'] = self.card

        # Definindo o RelativeLayout onde todo o corpo será posicionado
        relative = MDRelativeLayout()
        self.ids['relative'] = relative

        # Definindo o CircularProgressIndicator onde o usuário vai ter o carregamento visual
        circle = MDCircularProgressIndicator(
            size_hint=(None, None),
            size=("60dp", "60dp"),
            pos_hint={'center_x': .5, 'center_y': .6}
        )
        self.ids['progress'] = circle

        # Definindo o Label com texto carregando onde o usuário vai ter o indicador visual
        label = MDLabel(
            text='Carregando...',
            font_style='Title',
            halign='center',
            bold=True,
            text_color='black',
            pos_hint={'center_x': .5, 'center_y': .5}
        )
        self.ids['texto_carregando'] = label
        relative.add_widget(circle)
        relative.add_widget(label)
        self.card.add_widget(relative)

    def etapa1(self):
        if self.ids.diaria.text == '':
            self.ids.diaria.focus = True
        else:
            try:
                number = int(self.ids.diaria.text)
                print(number)
                self.etapa_1()
            except:
                print('Forneça um numero valido')

    def etapa_1(self):

        url = 'https://obra-7ebd9-default-rtdb.firebaseio.com/Funcionarios'
        data = {
            'Nome completo': self.nome,
            'Cpf do funcionario': self.cpf,
            'Pix do funcionario': self.pix,
            'Data de contratação': self.contratado,
            'Idade do funcionario': self.idade,
            'Contratante': self.contratante,
            'Valor da diaria': str(self.ids.diaria.text)
        }

        UrlRequest(
            f'{url}/.json',
            req_body=json.dumps(data),
            req_headers={'Content-Type': 'application/json'},
            on_success=self.etapa2
        )

    def etapa2(self, req, result):
        self.funcionario = result['name']
        progress = self.ids['progress']
        icon_acerto = self.ids['acerto']
        self.ids['relative'].remove_widget(progress)
        self.ids['relative'].add_widget(icon_acerto)
        self.ids.texto_carregando.text = 'Funcionario Cadastrado'
        self.ids.texto_carregando.pos_hint = {'center_x': .5, 'center_y': .55}
        self.add_widget(self.card)