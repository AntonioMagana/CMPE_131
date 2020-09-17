class Car():
    def factory(type):
        if type == "Racecar":
            return Racecar()
        elif type == Van:
            return Van()

    factory = staticmethod(factory)

class Racecar(Car):
    def drive(self):
        print("Racecar driving.")

class Van(Car):
    def drive(self):
        print("Van driving.")        

class main():
    driver = Car.factory("Racecar")
    driver.drive()