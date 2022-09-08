# Course: CSCI 256, Section 1
# Student Name: Visho Malla Oli
# Student ID: 010915723
# Program 1
# Due Date: Sept 9, 2022

# In keeping with the Honor Code of UM, I have neither given nor
# recieved assistance from anyone other than the TA or the instructor.

# Program Description: The program asks the user for how many cookies he/she wants to make
# and it displays the number of cups of each ingredient needed for the specified number of cookies.


# prompts for input
cook = int(input("Enter number of cookies you want to make: "))

# calculate number of cups of each ingredient needed
req_sugar = 1.5/48 * cook #returns the required sugar amount.
req_butter = 1/48 * cook #returns the required butter amount.
req_flour = 2.75/48 * cook #returns the required flour amount.

# display the output (2 decimal places)
print("\nUsing this cookie recipe, you need: ")
print(req_sugar, 'cups of sugar', sep = ' ')
print("%.2f" % req_butter, 'cups of butter', sep = ' ')
print(round(req_flour, 2), 'cups of flour', sep = ' ')
