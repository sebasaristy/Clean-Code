from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class TriquiApp( App ):

    def build(self):
        tablero = BoxLayout(orientation='vertical')

        fila1 = BoxLayout()
        for i in range(3):
            casilla = Button(text='')
            casilla.bind(on_press = self.callback)
            fila1.add_widget(casilla)

        tablero.add_widget(fila1)

        fila2 = BoxLayout()
        for i in range(3):
            casilla = Button(text='')
            casilla.bind(on_press = self.callback)
            fila2.add_widget(casilla)

        tablero.add_widget(fila2)


        fila3 = BoxLayout()
        for i in range(3):
            casilla = Button(text='')
            casilla.bind(on_press = self.callback)
            fila3.add_widget(casilla)

        tablero.add_widget(fila3)

        self.verificador = True

        return tablero
    

    def callback(self, sender):

        if self.verificador:
            self.verificador = False
            sender.text = 'X'

        else:
            self.verificador = True
            sender.text = 'O'
        

if __name__ == '__main__':
    TriquiApp().run()