from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class Calculator(GridLayout):

    def __init__(self, **kwargs):
        super(Calculator, self).__init__(**kwargs)
        self.cols = 4
        self.add_widget(Label(text="First Number:"))
        self.first_number = TextInput(multiline=False)
        self.add_widget(self.first_number)
        self.add_widget(Label(text="Second Number:"))
        self.second_number = TextInput(multiline=False)
        self.add_widget(self.second_number)
        self.add_widget(Label(text="Result:"))
        self.result = Label(text="")
        self.add_widget(self.result)
        self.add_widget(Button(text="+", on_press=self.addition))
        self.add_widget(Button(text="-", on_press=self.subtraction))

    def addition(self, instance):
        first = float(self.first_number.text)
        second = float(self.second_number.text)
        result = first + second
        self.result.text = str(result)

    def subtraction(self, instance):
        first = float(self.first_number.text)
        second = float(self.second_number.text)
        result = first - second
        self.result.text = str(result)

class CalculatorApp(App):

    def build(self):
        return Calculator()

if __name__ == "__main__":
    CalculatorApp().run()
