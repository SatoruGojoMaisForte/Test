from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.screen import MDScreen

class BricklayerScreen(MDScreen):
    nome = 'Custoviano lobo'
    avatar = 'https://res.cloudinary.com/dsmgwupky/image/upload/v1731366361/image_o6cbgf.png'

    def on_enter(self, *args):
        # Cabeçalhos da tabela
        column_data = [("Nome", dp(150)), ("Idade", dp(50)), ("Email", dp(200))]
        row_data = [
            ("João", "25", "joao@example.com"),
            ("Maria", "30", "maria@example.com"),
            ("Pedro", "22", "pedro@example.com")
        ]



