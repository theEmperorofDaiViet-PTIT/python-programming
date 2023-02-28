class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def fill_gas_tank(self, status):
        print(f"This car has {status} gas tanks!")

class Battery():
    def __init__(self, battery_size=75, weight = 100):
        self.battery_size = battery_size
        self.weight = weight

    def describe_battery(self):
        print(f"This car has a {self.battery_size} - kwh battery.")
        print(f"This battery is {self.weight} kilograms")

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year, color):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.color = color
        self.battery_size = Battery(150, 1000)

    def fill_gas_tank(self):
        print("This car doesn't gas tank!")
        
    def describe_color(self):
        print(f"This car has {self.color}")

my_tesla = ElectricCar("tesla", 'model s', 2019, 'white')
print(my_tesla.get_descriptive_name())
my_tesla.describe_color()
my_tesla.battery_size.describe_battery()










