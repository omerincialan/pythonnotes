##
#  A program to compute shipping costs.
#

# Obtain the user input.
country = input("Enter the country: ")
state = input("Enter the state or province: ")

# Compute the shipping cost.
shippingCost = 0.0

if country == "USA" :
   if state == "AK" or state == "HI" :  # See Section 3.7 for the or operator
      shippingCost = 10.0
   else :
      shippingCost = 5.0
else :
   shippingCost = 10.0

# Print the results.
print("Shipping cost to %s, %s: $%.2f" % (state, country, shippingCost))

