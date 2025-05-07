##
#  This module defines an employee class hierarchy for payroll processing. 
#

## An employee has a name and a mechanism for computing weekly pay.
#
class Employee :
   ## Constructs an employee with a given name.
   #  @param name the name of the employee
   #
   def __init__(self, name) :
      self._name = name

   ## Gets the name of this employee.
   #  @return the name 
   #
   def getName(self) :
      return self._name

   ## Computes the pay for one week of work.
   #  @param hoursWorked the number of hours worked in the week
   #  @return the pay for the given number of hours
   #
   def weeklyPay(self, hoursWorked) :
      return 0.0


## An hourly employee is paid for every hour worked.
#
class HourlyEmployee(Employee) :
   ## Constructs an hourly employee with a given name and hourly wage.
   #  @param name the name of this employee
   #  @param wage the hourly wage
   #
   def __init__(self, name, wage) :
      super().__init__(name)
      self._hourlyWage = wage
 
   # Overrides the superclass method.
   def weeklyPay(self, hoursWorked) :
      pay = hoursWorked * self._hourlyWage
      if hoursWorked > 40 :
         # Add overtime.
         pay = pay + ((hoursWorked - 40) * 0.5) * self._hourlyWage
      return pay


## A salaried employee is paid the same amount independent of the hours worked.
#
#
class SalariedEmployee(Employee) :
   ## Constructs a salaried employee with a given name and annual salary.
   #  @param name the name of this employee
   #  @param salary the annual salary
   #
   def __init__(self, name, salary) :
      super().__init__(name)
      self._annualSalary = salary

   # Overrides the superclass method.
   def weeklyPay(self, hoursWorked) : 
      WEEKS_PER_YEAR = 52
      return self._annualSalary / WEEKS_PER_YEAR
      
      
## A manager is a salaried employee who also receives a bonus.
#
class Manager(SalariedEmployee) :
   ## Constructs a manager with a given name, annual salary, and weekly bonus.
   #  @param name the name of this employee
   #  @param salary the annual salary
   #  @param bonus the weekly bonus
   #
   def __init__(self, name, salary, bonus) :
      super().__init__(name, salary)
      self._weeklyBonus = bonus
   
   # Overrides the superclass method.
   def weeklyPay(self, hoursWorked) :
      return super().weeklyPay(hoursWorked) + self._weeklyBonus
      

