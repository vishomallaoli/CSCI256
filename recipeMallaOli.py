# inputs
cook = int(input("Enter number of cookies you want to make: "))

# calculations
req_sugar = 1.5/48 * cook #returns the required sugar amount.
req_butter = 1/48 * cook #returns the required butter amount.
req_flour = 2.75/48 * cook #returns the required flour amount.

# results
print("\nUsing this cookie recipe, you need: ")
print(req_sugar, 'cups of sugar', sep = ' ')
print("%.2f" % req_butter, 'cups of butter', sep = ' ')
print(round(req_flour, 2), 'cups of flour', sep = ' ')