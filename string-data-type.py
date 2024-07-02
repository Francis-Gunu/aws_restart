myString = "This is a string"
print(myString)
print(type(myString))
print(myString + " is the data type " + str(type(myString)))

firstString = "water"
secondString = "fall"
thirdString = firstString + secondString

print(thirdString)

name = input("what is my name?")
print(name)

color = input("what is my favorite color? ")
animal = input("what is my favorite animal? ")
print("{}, you like a {} {}!" .format(name,color,animal))