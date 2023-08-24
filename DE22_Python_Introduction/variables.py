# SOURCE: https://www.youtube.com/watch?v=LKFrQXaoSMQ           (13:30 MIN)
# variable =    a reusable container for storing a value
#               a variable behaves as if it were the value it contains

print(f"Variable examples:")

age = 21
print(age)

print("You are " + str(age) + " years old")     # String concatenation
print("You are", age, "years old")              # Separate arguments
print(f"You are {age} years old")               # F-Strings
print("-----------")

# INTEGER
print(f"Integer variable examples:")

age == 21
players = 2
quantity = 5

print(f"You are {age} years old")
print(f"There are {players} online")
print(f"You would like to buy {quantity} items")
print("-----------")
# FLOAT
print(f"Float variable examples:")
gpa = 3.2
distance = 2.5
price = 10.99

print(f"Your gpa is {gpa}")
print(f"You ran {distance} Km")
print(f"The  prise is ${price}")
print("-----------")

# STRINGS
print(f" Strings variable examples:")

name = "Bro"
food = "pizza"
email = "bro1233@gmail.com"


print(f"Hello {name}")
print(f"You like {food}")
print(f"Your email is: {email}")

print("-----------")

# BOOLEAN (true/false) are most often used "internally"
# COMMOON MISTAKE: Booleans are not written online ="True" because it is then treated as a string
print(f"Boolean variable examples:")

online = True
for_sale = False
running = True
print(f"Are you online?: {online}")
print(f"Is the item for sale?: {for_sale}")
print(f"Game running: {running}")

if running:
    print("The game is running")
else: print("The game is over")

print("-----------")
# VARIABLES TIPS AND TRICKS
# instead of declaring xyz as
    # x = 1
    # y = 2
    # z = 3
# you can use multiple assignment as below
x, y, z = 1, 2, 3

# you can also do this:
x = y = z = 0   # sets all the variables to the same value.

print(x)
print(y)
print(z)

