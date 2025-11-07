import os
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.core.window import Window


class CalculadoraBox(BoxLayout):
    def borrar_uno(self):
        texto = self.ids.entrada.text
        self.ids.entrada.text = texto[:-1]


    def limpiar_todo(self):
        self.ids.entrada.text = ""

    def agregar(self, valor):
        self.ids.entrada.text += valor

    def igual(self):
        try:
            expresion = self.ids.entrada.text.replace("/", "//")
            resultado = str(eval(expresion))
            self.ids.entrada.text = resultado
        except Exception:
            self.ids.entrada.text = "Syntax ERROR"
    
class Calculadora1App(App):
    def build(self):
        self.title = "Calculadora CBTA"
        self.icon = "cbta.jpg"

        Window.size = (370, 450)
        Window.clearcolor = (0/255, 0/255, 50/255, 1)
        Window.resizable = False
        kv_path = os.path.join(os.path.dirname(__file__), 'calculadora.kv')
        Builder.load_file(kv_path)
        return CalculadoraBox()

if __name__ == '__main__':
    Calculadora1App().run()