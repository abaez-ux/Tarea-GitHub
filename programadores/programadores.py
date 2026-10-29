import os

from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.uix.card import MDCard
from kivymd.uix.screen import MDScreen

# Carga el archivo programadores.kv, que está en esta misma carpeta.
Builder.load_file(os.path.join(os.path.dirname(__file__), "programadores.kv"))

# Carpeta images, ubicada dentro de la carpeta principal del proyecto.
CARPETA_IMAGENES = os.path.join(os.path.dirname(os.path.dirname(__file__)), "images")

# Integrantes del grupo. Se intentan reconocer las fotos por el nombre del archivo.
# Si no se reconoce el nombre, se usan las fotos disponibles en orden alfabético.
INTEGRANTES = [
    {"nombre": "Juan Manuel Fernández Carbia", "curso": "4to B Informática", "foto": "carbia.png"},
    {"nombre": "Franco Nahuel Ferreyra", "curso": "4to B Informática", "foto": "proyecto/images/WhatsApp Image 2026-10-25 at 14.35.10.jpeg"},
    {"nombre": "Alejandro Baez Lopez", "curso": "4to B Informática", "foto": "ale.png"},
    {"nombre": "Juan Cruz Guillén", "curso": "4to B Informática", "foto": "proyecto/images/WhatsApp Image 2026-10-25 at 14.32.46.jpeg"},
]


def buscar_foto(nombre, indice):
    """Busca la foto indicada; si el nombre varía, usa otra foto disponible."""
    extensiones = (".png", ".jpg", ".jpeg", ".webp")
    disponibles = sorted(
        archivo for archivo in os.listdir(CARPETA_IMAGENES)
        if archivo.lower().endswith(extensiones)
        and archivo.lower() != "avatar.png"
    ) if os.path.isdir(CARPETA_IMAGENES) else []

    # Primero intenta el nombre configurado, sin distinguir mayúsculas/minúsculas.
    buscado = nombre.lower()
    for archivo in disponibles:
        if archivo.lower() == buscado:
            return os.path.join(CARPETA_IMAGENES, archivo)

    # Después intenta encontrar un archivo relacionado con el apellido/nombre.
    claves = {
        0: ("carbia", "juanmanuel", "juan_manuel"),
        1: ("ferreyra", "franco"),
        2: ("ale", "baez", "baezlopez", "alejandro"),
        3: ("guillen", "guillén", "juanc", "juancruz"),
    }.get(indice, ())
    for archivo in disponibles:
        base = os.path.splitext(archivo.lower())[0]
        if any(clave in base for clave in claves):
            return os.path.join(CARPETA_IMAGENES, archivo)

    # Último recurso: asigna una foto disponible por orden alfabético.
    if indice < len(disponibles):
        return os.path.join(CARPETA_IMAGENES, disponibles[indice])

    # Si no hay foto propia para este integrante, utiliza la imagen de ejemplo.
    return os.path.join(CARPETA_IMAGENES, "avatar.png")


class TarjetaIntegrante(MDCard):
    # Datos que muestra cada tarjeta (se usan en programadores.kv).
    nombre = StringProperty()
    curso = StringProperty()
    foto = StringProperty()


class ProgramadoresScreen(MDScreen):
    def on_kv_post(self, base_widget):
        # Crea una tarjeta por cada integrante.
        for indice, integrante in enumerate(INTEGRANTES):
            tarjeta = TarjetaIntegrante(
                nombre=integrante["nombre"],
                curso=integrante["curso"],
                foto=buscar_foto(integrante["foto"], indice),
            )
            self.ids.lista.add_widget(tarjeta)

    def volver(self):
        self.manager.current = "inicio"
