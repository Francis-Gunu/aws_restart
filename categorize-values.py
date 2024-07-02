#  Creating a mixed-type list and useing a for loop statement to traverse the list and print the data type for each item in the list

mymixedtypelist = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]
print(type(mymixedtypelist))

for item in mymixedtypelist:
    
    print("{} of the type of data {}" .format(item,type(item)))