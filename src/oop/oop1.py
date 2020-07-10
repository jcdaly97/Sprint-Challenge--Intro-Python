# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class
#parent class 
class Vehicle:
    pass

#child of vehicle 
class FlightVehicle(Vehicle):
    pass

#child of vehicle
class GroundVehicle(Vehicle):
    pass

#grandchild of vehicle, child of FlightVehicle
class Starship(FlightVehicle):
    pass

#grandchild of vehicle, child of FlightVehicle
class Airplane(FlightVehicle):
    pass

#grandchild of vehicle, child of GroundVehicle
class Motorcycle(GroundVehicle):
    pass

#grandchild of vehicle, child of GroundVehicle
class Car(GroundVehicle):
    pass