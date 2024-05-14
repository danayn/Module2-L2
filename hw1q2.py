# 2. The Greatest Showdown

# Objective:
# Harness the power of conditional statements to compare and determine values.

'''
Task 1: Identify the Greatest
Write a Python program that prompts the user to enter three numbers. 
The program should then identify and print out the largest number among the three.

Task 2: Identify the Smallest
Extend your program from Task 1 to also determine the smallest number among the three and print it out.

Task 3: Equality Check
Enhance your program to handle cases where two or all of the numbers are equal. 
The program should display appropriate messages like "Two numbers are equal and the largest" or "All numbers are equal".

Expected Outcome: If we provide the numbers 3, 3, and 4, it should print out that "The smallest number is 3. 
The largest number is 4. There are two numbers equal to each other." 
Printing out which numbers are equal would be a great added bonus.

'''

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

#Identify the Greatest
print("The largest number among the three is printed below.")
if (num1 >= num2 and num1 >= num3):
    print(num1)
elif (num2 >= num1 and num2 >= num3):
    print(num2)
elif (num3 >= num1 and num3 >= num2):
    print(num3)
print(" ")

#Identify the Smallest
print("The smallest number among the three is printed below.")
if (num1 <= num2 and num1 <= num3):
    print(num1)
elif (num2 <= num1 and num2 <= num3):
    print(num2)
elif (num3 <= num1 and num3 <= num2):
    print(num3)
print(" ")

#Equality Check
print("This is the Equality Check.")
if(num1 == num2 == num3):
    print("All numbers are equal.")
if(num1 == num2 or num2 == num3 or num3 == num1):
    print("There are two numbers equal to each other.")
if(num1 != num2 != num3):
    print("None of the numbers are equal to each other.")
    