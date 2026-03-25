from kivy.app import App

from kivy.uix.label import Label

class HelloApp(App):
    def build(self):
        return Label(text='Hola mundo', font_size=100, color=(1, 0, 0, 1))
    
if __name__ == '__main__':
    HelloApp().run()