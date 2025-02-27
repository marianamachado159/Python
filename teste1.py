from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        layout = BoxLayout()
        btn = Button(text="Clique Aqui")
        layout.add_widget(btn)  # Adicionando o botão ao layout
        return layout

MyApp().run()