class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg

    def display_car(self):
        return ("This is a %s %s with %d MPG." % (self.color, self.model, self.mpg))

    def drive_car(self):
        self.condition = "used"


my_car = Car("DeLorean", "silver", 88)
print my_car.condition
my_car.drive_car()
print my_car.condition
