class Car(object):
    def __init__(self, color, doors, tires):
         self.color = color
         self.doors = doors
         self.tires = tires
    def stoptheCar(self):
        return "Stop the car"

    def drive(self):
        return "Go on!!!"

a = Car("black", 4, 4)
print(a.color, a.doors, a.tires)
print(a.drive())
print(a.stoptheCar())







