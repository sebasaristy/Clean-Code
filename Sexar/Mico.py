from kivy.app import App

from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image

class MicoApp(App):
    def build(self):
        contenedor = BoxLayout(orientation='vertical')
        
        # Cargar imagen desde tu PC
        imagen = Image(source=r'C:\Users\user\Downloads\la_k.jpeg', size_hint_y=3)
        contenedor.add_widget(imagen)
        
        self.textinput = TextInput(text='Hola mundo')
        self.etiqueta = Label(text = 'Hola mundo')
        contenedor.add_widget(self.etiqueta)
        contenedor.add_widget(self.textinput)

        boton = Button(text='Boton')
        boton.bind(on_press=self.callback)
        contenedor.add_widget(boton)

        return contenedor
    
    def callback(self, sender):
        print('Boton presionado')
        self.etiqueta.text = self.textinput.text


if __name__ == '__main__':
    MicoApp().run()