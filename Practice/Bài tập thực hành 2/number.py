class Number():
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2
    
    def input_info(self):
        print(f"Input number is {self.number1} and {self.number2}")
    
    def addition(self):
        return self.number1 + self.number2
    
    def subtract(self):
        return self.number1 - self.number2
    
    def multi(self):
        return self.number1*self.number2
    
    def division(self):
        return self.number1/self.number2

number = Number(13, 5)
number.input_info()
print(number.subtract())
print(number.addition())