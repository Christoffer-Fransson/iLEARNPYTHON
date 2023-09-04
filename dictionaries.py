# Video: https://www.youtube.com/watch?v=MZZSMaEAC2g (8:05) min

# dictionary = a collection of {key:value} pairs
#              ordered and changeable. No duplicates

capitals = {"USA": "Washington", "India": "New Delhi", "China": "Beijing",}

# print(dir(capitals))    # lists the various actions in the dictionary in question
# print(help(capitals))     # not really working, import problems??

# print(capitals.get("USA"))  # prints The associated value with the key (Washington)


# if capitals.get("India"):
#     print("that capital exists")
# else:
#     print("That capital doesn't exists")
    
    
# capitals.update({"Germany": "Berlin"})  # Updates with new key value pair or updates existing ones. NOTE: Never do this during iterative loop!

# capitals.pop("China")  # Removes China key value
# capitals.clear()        # clears the dictionary

# keys = capitals.keys()          # gets the key value
# for key in capitals.keys():
#     print(key)
    
# values = capitals.values()      # gets all values
# for value in capitals.values():
#     print(values)    


for key, value in capitals.items():         # gets all items returns a 2-dimensional list type
    if key == "India" and value == "New Delhi":
        print("Remove this")

 