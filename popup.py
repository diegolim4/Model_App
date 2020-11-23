from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup


class TelaInicial(BoxLayout):
    def pop(self):
        caixa = BoxLayout(padding=10)
        btn = BoxLayout()

        pops = Popup(title='Hello Word', content=caixa, size_hint=(None, None), size=(200, 150), auto_dismiss=False)

        fecha = Button(text='Fecha', on_press=pops.dismiss)

        btn.add_widget(fecha)

        caixa.add_widget(btn)

        pops.open()


class Testpopup(App):
    def build(self):
        return


Testpopup().run()
