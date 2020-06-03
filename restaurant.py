class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"\n{self.restaurant_name} serves {self.number_served} customers with {self.cuisine_type}")

    def open_restaurant(self):
        print(f"\n{self.restaurant_name} is now open")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, increment_number_served):
        #self.increment_number_served = number_served +
        self.number_served += increment_number_served

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = 'flavours'




new_rest = Restaurant('Sizzler', 'Variety')
