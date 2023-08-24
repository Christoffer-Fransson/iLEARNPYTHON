# SOURCE: https://www.youtube.com/watch?v=Qtq83lAoogM       (7:36 MIN)
# typecasting = The process of converting a value of one data type to another type 
#               (string, integer, float, boolean)
#                Explicit vs Implicit


name ="Bro"
age = 21
gpa = 1.9
student = True

type(name)                  #function to return what type the variable contain
print(type(name))           # need a print or similar function to print out the return. eg. <class 'str'> for string, <class 'int'> for integer, <class 'float'> for float and <class 'bool'> for boolean.

print(type(name))
print(type(age))
print(type(gpa))
print(type(student))
print("---------------")

# EXPLICIT CAST
print("Explicit type casting examples:")
# integer -> float
age = float(age)            # changes datatype to float
print(age)                  # age is now 21.0
print(type(age))
print("------")

# float -> integer
gpa = int(gpa)              # change datatype to integer
print(gpa)                  # a float cannot be contained in a integer so it is truncated into the first number eg. 1.9 -> 1        
print("------")

# boolean -> string
student = str(student)      # change datatype to integer
print(student)
print(type(student))
print("------")

# integer -> boolean        
age = bool(age)              # change datatype to integer          
print(age)                   # any value other than zero = true, zeroe = false
print(type(age))

# IMPLICIT CAST
print("Implicit casting examples:")
x= 2
y= 2.0

x= x / y
print(x)                    # a variable's datatype can be converted when you do certain operations on it eg. arithmatic operations.



