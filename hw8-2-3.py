 #Write a program that prompts the user to enter a list of 5 numbers separated by spaces 
 #and then calculates the sum of all the numbers in the list.

#Author: ALJ (AMDG) 10/17/20
#if needed, https://www.pythonforbeginners.com/dictionary/python-split
#it changes a str to a list and breaks at the space if nothing is specified

numbers = input("Please input a list of 5 numbers separated by spaces: ")

list1 = numbers.split()

int1 = list1[0]
int2 = list1[1]
int3 = list1[2]
int4 = list1[3]
int5 = list1[4]

sum1 = int(int1) + int(int2) + int(int3) + int(int4) + int(int5)
print("The sum of the integers from the list you entered is " + str(sum1) + ".")