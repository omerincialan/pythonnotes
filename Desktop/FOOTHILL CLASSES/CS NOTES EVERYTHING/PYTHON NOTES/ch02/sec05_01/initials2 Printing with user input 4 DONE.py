##
#  This program obtains two names from the user and prints a pair of initials.
#

# Obtain the two names from the user.
first = input("Enter your first name: ")
second = input("Enter your significant other's first name: ")

# Compute and display the initials.
initials = first[0] + "&" + second[0]
print(initials)

