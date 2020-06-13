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


my_car = Car("DeLorean", "silver", 88)
print(my_car.condition)
my_car.driver_car()
print(my_car.condition)
my_car.display_car()
