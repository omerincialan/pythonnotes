##
#  Compute the discount for a given purchase.
#

# Obtain the original price.
originalPrice = float(input("Original price before discount: "))

# Determine the discount rate.
if originalPrice < 128 :
   discountRate = 0.92
else :
   discountRate = 0.84

# Compute and print the discount.
discountedPrice = discountRate * originalPrice
print("Discounted price: %.2f" % discountedPrice)

