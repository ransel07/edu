from kivy.app import App
from kivy.uix.button import Button

class User_Interfase(App):
    def build(self):
        return Button(text= "click", font_size=24)

if __name__ == '__main__':
    User_Interfase().run()
