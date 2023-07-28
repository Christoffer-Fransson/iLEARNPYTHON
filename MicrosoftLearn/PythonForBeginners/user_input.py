# This file shows how to ask for user input and put it into a program

print("Welcome to the greeter program")
name = input("Enter your name: ")
print("Greetings " + name)


# example (that will not work as expected) reason: input datatype is a string and not eg integer. so print concatenates
# print("calculator program")
# first_number = input("first number: ")
# second_number = input("second number: ")
# print(first_number + second_number)

# example that works as intended
print("Calculator Program")
first_number = input("First number: ")
second_number = input("second number: ")
# print("Sum: " + int(first_number) + int(second_number)) # this does not work on runtime because print is trying to concatenate two DIFFEREJT datatypes
print("Sum: " + str(int(first_number) + int(second_number))) # this works because "Sum " " is a string and the integers are converted into string which is then concatenated"
