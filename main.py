from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
import math

#set the app size
Window.size=(500,700)

Builder.load_file('calc.kv')

class MyLayout(Widget):
    def clear(self):
        self.ids.calc_input.text='0'
        
    def button_press(self,button):
        prior=self.ids.calc_input.text
        
        if prior =="0":
            self.ids.calc_input.text=''
            self.ids.calc_input.text=f'{button}'
        else:
            self.ids.calc_input.text=f'{prior}{button}'
    
    def dot(self):
        prior=self.ids.calc_input.text
        if "." in prior:
            pass
        else:
            prior=f'{prior}.'
            self.ids.calc_input.text=prior
    
    def remove(self):
        prior=self.ids.calc_input.text
        prior=prior[:-1]
        self.ids.calc_input.text=prior
    
    def signchange(self):
        prior=self.ids.calc_input.text
        if prior[0]=="-":
            prior=prior[1:]
            self.ids.calc_input.text=f'{prior}'
        else:
            self.ids.calc_input.text=f'-{prior}'
            
    def math_sign(self,sign):
        prior=self.ids.calc_input.text
        listsign=["*","+","-","/"]
        if prior[-1] in listsign:
            pass
        else:
            self.ids.calc_input.text=f'{prior}{sign}'
        
    def equals(self):
        prior=self.ids.calc_input.text
        self.ids.calc_input.text=str(eval(prior))    

class CalculatorApp(App):
    def build(self):
        return MyLayout()
    
if __name__=="__main__":
    CalculatorApp().run()