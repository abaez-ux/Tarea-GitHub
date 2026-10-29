import os
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

Builder.load_file(os.path.join(os.path.dirname(__file__), "login.kv"))

class LoginScreen(MDScreen):
    def volver(self):
        self.manager.current = "inicio"

    def iniciar_sesion(self):
        # Por ahora no se valida el usuario; se conectará con la base de datos más adelante.
        self.manager.current = "home"
