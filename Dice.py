from random import  randint

class Die:
    def __init__(self, sides = 6):
        self.sides = sides

    def roll_die(self):
        return randint(0,self.sides)

dice1 = Die(500)

x = 0
while x < 11:
    print(dice1.roll_die())
    x += 1
