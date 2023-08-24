# Exercise goal is to use the parsec to lightyear (earlier built see WorkWithOutput exercise)

# Build a unit converter based on input
print("Enter how many parsecs to convert:(whole numbers only)") 
parsecs_input = input("# of Parsecs: ") # User can input the number of parsecs here. NOTE: no error handling if user inputs a non integer value.
parsecs = int(parsecs_input) # Convers user inputed value into a integer datatype
lightyears = parsecs * 3.26 # multiplies the integervalue with the hardcoded parsec to lightyear conversion rate.
print((str(parsecs)) + " parsecs is " + str(lightyears) + " lightyears") # Outputs Nr of parsecs and how many lightyears they are.
