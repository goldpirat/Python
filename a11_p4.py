# CTMS-14
# a11_p4.py
# Hannah Paulus
# hpaulus@constructor.university

# creating the Vehicle class
class Vehicle():
    # initializing the class with name, max speed and mileage
    def __init__(self, name, max_speed, mileage):
        self._name = name
        self._maxspeed = max_speed
        self._mileage = mileage
    
    def getname(self): # getter for the name
        return self._name
    
    # Returning a string of the class description for any object of this class
    def __str__(self):
        return "Vehicle with a max speed capacity of " + str(self._maxspeed) + \
               " and " + str(self._mileage) + " of mileage"


# creating a child class of Vehicle parent class called Bus
class Bus(Vehicle):
    #initializing the class with name, max speed and mileage using parent class
    def __init__(self, name, max_speed, mileage):
        Vehicle.__init__(self, name, max_speed, mileage)

    def getname(self): # using the getname method from parent class
        return Vehicle.getname(self)
    def __str__(self):
        return "Bus with a max speed capacity of " + str(self._maxspeed) + \
               " and " + str(self._mileage) + " of mileage"

# creating vehicle objects
first_vehicle = Vehicle("Renault 5", 240, 50000)
second_vehicle = Vehicle("Mercedes ML 2012", 275, 60000)
# creating bus objects
first_bus = Bus("School Bus", 110, 155550)
second_bus = Bus("Auto Bus", 160, 5000)

# printing the objects with the specific information
print("Vehicles:")
print(first_vehicle.getname(),":", first_vehicle)
print(second_vehicle.getname(),":", second_vehicle)

# printing the object with the specific information
print("Buses:")
print(first_bus.getname(),":", first_bus)
print(second_bus.getname(),":", second_bus)