class Lunch:
    def __init__(self, menu):
        self.menu = menu

    def menu_price(self):
        if "menu 1":
            print(f"Your choice: {self.menu}, Price 12.00")
        elif "menu 2":
            print(f"Your choice: {self.menu}, Price 13.40")
        else:
            print("Error in Menu")

Paul = Lunch("menu 1")

Paul.menu_price()
