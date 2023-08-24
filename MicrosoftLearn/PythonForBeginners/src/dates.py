# THIS FILE CONTAIN INFORMATION ABOUT PYTHON AND DATE HANDLING WITH EXAMPLES (IF APPLICABLE)

# To work with a date you need to import the > date < module 

from datetime import date # Imports the date function that can now be used
date.today() # The function for getting todays date note: this is local system time
print(date.today())

# Date type conversion
# print("Today's date is: " + date.today()) # This does not work and generates type error. 
                                            # you cannot combine two different datatypes eg a string (text) with a date

# To solve this convert the date into a string using str()
print("Today's date is: " + str(date.today()))

