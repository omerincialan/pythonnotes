## 
#  This module defines the CashRegister class.
#

## A simulated cash register that tracks the item count and the total amount due.
#
class CashRegister :
   ## Constructs a cash register with cleared item count and total.
   #  @param taxRate the tax rate to use with this cash register
   #
   def __init__(self, taxRate) :
      self._itemCount = 0
      self._totalPrice = 0.0
      self._taxableTotal = 0.0
      self._taxRate = taxRate
      
   ## Adds an item to this cash register.
   #  @param price the price of this item
   #  @param taxable True if this item is taxable
   #
   def addItem(self, price, taxable) :
      self._itemCount = self._itemCount + 1
      self._totalPrice = self._totalPrice + price
      if taxable :
         self._taxableTotal = self._taxableTotal + price
      
   ## Gets the price of all items in the current sale.
   #  @return the total price
   #
   def getTotal(self) :
      return self._totalPrice + self._taxableTotal * self._taxRate / 100
      
   ## Gets the number of items in the current sale.
   #  @return the item count
   #
   def getCount(self) :
      return self._itemCount

   ## Clears the item count and the total.
   #  
   def clear(self) :
      self._itemCount = 0
      self._totalPrice = 0.0
      self._taxableTotal = 0

