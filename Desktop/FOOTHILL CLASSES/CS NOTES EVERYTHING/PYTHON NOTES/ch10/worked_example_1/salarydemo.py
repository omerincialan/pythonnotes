##
#  This program demonstrates polymorphism by applying a method
#  to objects of different classes.
#

from employees import HourlyEmployee, SalariedEmployee, Manager

staff = []
staff.append(HourlyEmployee("Morgan, Harry", 30.0))
staff.append(SalariedEmployee("Lin, Sally", 52000.0))
staff.append(Manager("Smith, Mary", 104000.0, 50.0))
      
for employee in staff :
   hours = int(input("Hours worked by " + employee.getName() + ": "))
   pay = employee.weeklyPay(hours)
   print("Salary: %.2f" % pay)

