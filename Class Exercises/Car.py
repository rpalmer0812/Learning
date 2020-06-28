class Car:
    def __init__(self, model, colour, mpg):
        self.model = model
        self.colour = colour
        self.mpg = mpg
    condition = "new"

    def display_car(self):
        print(f"This is a {self.colour} {self.model} with {self.mpg} MPG.")

    def driver_car(self):
        self.condition = "used"

class ElectricCar(Car):
    condition = "new"
    def __init__(self, model, colour, mpg, battery_type):
        self.model = model
        self.colour = colour
        self.mpg = mpg
        self.battery_type = battery_type

    def driver_car(self):
        self.condition = "like new"



my_car = ElectricCar("DeLorean", "silver", 88, "molten salt")
print(my_car.condition)
my_car.driver_car()
print(my_car.condition)
my_car.display_car()

print(my_car.battery_type)
print(my_car.condition)
my_car.driver_car()
print(my_car.condition)
