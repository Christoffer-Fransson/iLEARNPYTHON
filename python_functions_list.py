
# daterelated - see more under PythonForBeginners/dates.py
from datetime import date # Imports the date function that can now be used
date.today() # The function for getting todays date note: this is local system time


#input
input() # the import function stores a result as a string and NOT a number eg. variable a + variable B -> ab and not mathematical a + b
print("Welcome to the greeter program")
name = input("Enter your name: ")
print("Greetings " + name)

#int()
int() # function similar to str() that converts the datatype (variable) specifid into a integer datatype. Variable A + Variable B = C (mathematical sum of a +b)

#print
print("") # prints text in console
print('') # '' can be used instead of "" if the text contains "" which would invalidate syntax

# str() - Datatype conversion into string
str() # Converts into a string data type. 
str(date.today())

