#Author: ALJ (AMDG) 11/17/20
numbers = input("Please enter 5 digits with no separation: ")

list1 = list(numbers)
list2 = list(numbers)

list2.sort()

if list2 == list1:
    print("The numbers you entered are sorted!")
else:
    print("The numbers you entered are not sorted.")


#CODE: if separation is needed
#numbers = input("Please enter 5 numbers (no commas please"): )
#list1 = numbers.split()
#list2 = numbers.split()

#list1.sort()

#if list2 == list1:
    #print("The numbers you entered are sorted!")
#else:
    #print("The numbers you entered are not sorted.")