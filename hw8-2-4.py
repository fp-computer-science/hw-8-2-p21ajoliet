#Author: ALJ (AMDG) 11/17/20
input1 = input("Please enter a list of numbers or letters separated by spaces: ")
print(" ")
print("Please enter either \'middle' or \'ends' for the following question.")
print(" ")

input2 = input("Would you like the program to return the MIDDLE or the ENDS of your first list? ")

inputa = input2.lower()
e = "ends"
m = "middle"

#middle
middle = input1.split()
del middle[0]
middle.reverse()
del middle[0]
middle.reverse()

#ends
list1 = input1.split()
liste1 = list1[0]
list1.reverse()
liste2 = list1[0]
end = str(liste1) + ' ' + str(liste2)
ends = end.split()

if inputa == e:
    print(ends)
elif inputa == m:
    print(middle)
else:
    print("I messed up, sorry.")