## 
#  This program tests the enhanced CashRegister class.
#

from cashregister2 import CashRegister

register1 = CashRegister(7.5)
register1.addItem(3.95, False)
register1.addItem(19.95, True)
print(register1.getCount())
print("Expected: 2")
print("%.2f" % register1.getTotal())
print("Expected: 25.40")

