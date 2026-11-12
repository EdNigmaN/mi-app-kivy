import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class MiApp(App):
    def build(self):
        # Creamos un layout vertical
        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        
        # Etiqueta inicial
        self.etiqueta = Label(text='¡Hola desde Kivy!', font_size='30sp')
        layout.add_widget(self.etiqueta)
        
        # Botón que cambia el texto
        boton = Button(text='Púlsame', font_size='24sp', size_hint=(1, 0.4))
        boton.bind(on_press=self.cambiar_texto)
        layout.add_widget(boton)
        
        return layout
    
    def cambiar_texto(self, instance):
        if self.etiqueta.text == '¡Hola desde Kivy!':
            self.etiqueta.text = '¡Funciona! 🎉'
        else:
            self.etiqueta.text = '¡Hola desde Kivy!'

if __name__ == '__main__':
    MiApp().run()