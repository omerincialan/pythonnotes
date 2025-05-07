##
#  This module defines classes that model vehicle classes.
#

## A generic vehicle superclass.
#
class Vehicle :
   ## Constructs a vehicle object with a given number of tires.
   #  @param numberOfTires the number of tires on the vehicle
   #
   def __init__(self, numberOfTires) :
      self._numberOfTires = numberOfTires
      
   ## Gets the number of tires on the vehicle.
   #  @return number of tires
   #
   def getNumberOfTires(self) : 
      return self._numberOfTires 

   ## Changes the number of tires on the vehicle.
   #  @param newValue the number of tires
   #
   def setNumberOfTires(self, newValue) :
      self._numberOfTires = newValue
      
   ## Gets a description of the vehicle.
   #  @return a string containing the description
   #
   def getDescription(self) :
      return "A vehicle with " + self._numberOfTires + " tires"


## A specific type of vehicle - car.
#
class Car(Vehicle) :
   ## Constructs a car object.
   #
   def __init__(self) :
      # Call the superclass constructor to define its instance variables.
      super().__init__(4)
      
      # This instance variable is set by the subclass.
      self._plateNumber = "??????"

   ## Sets the license plate number of the car.
   #  @param newValue a string containing the number
   #
   def setLicensePlateNumber(self, newValue) :
      self._plateNumber = newValue

   ## Gets a description of the car.
   #  @return a string containing the description
   #
   def getDescription(self) : 
      return "A car with license plate " + self._plateNumber

