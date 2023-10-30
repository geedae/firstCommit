class Car:
    def __init__(self, color, milage, engin_type, name, make):
        self.color = color
        self.milage = milage
        self.engin_type = engin_type
        self.name = name 
        self.make = make

    def move(self):
        print(f"{self.name} is a {self.make} product and it is moving")

    def stop(self):
        print(f"{self.name} is a {self.make} product and has stopped")


class Automatic(Car):
    def __init__(self, color, milage, engin_type, name, make, leather_seat):    #### is the atribut of the child class 
        super().__init__(color, milage, engin_type, name, make)   #### is making sure it inherites atribute from the parent class 
        self.leathe_seat = leather_seat

    def fly(self):
        print("The {} car is a {}, it is {} that is has leather seat and it can fly".format(self.name, self.make, self.leathe_seat))

my_car1 = Car("blue", 12, "V12", "AMG", "Benz")

# my_car2 =Car("red", 34, "V4", "Camry","Toyota")

# my_car1.stop()

nice_car = Automatic("red", 34, "V4", "Camry","Toyota", True)
# nice_car.move()     
nice_car.fly()                

## POLYMORPHISM                    
                     
