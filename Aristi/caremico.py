from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class HelloApp(App):
    def build(self):
        self.textInput = TextInput()
        self.etiqueta = Label(text='Hola.')
        boton = Button(text='Saludar')

        boton.bind(on_press=self.callback)
    
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.textInput)
        layout.add_widget(self.etiqueta)
        layout.add_widget(boton)


        return layout
    
    def callback(self, sender):
        self.etiqueta.text = f'Hola {self.textInput.text}. Espero que tengas un buen día.'

if __name__ == '__main__':
    HelloApp().run()