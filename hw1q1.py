# 1. Decisions at the Crossroad

# Task 1: Code Correction
#You are provided with a Python script that uses conditional statements to tell 
#if a number is positive, negative, or zero, but it has some errors. Identify and fix them.

#code with fixed errors below ---->
# The first one is not putting int() before input(). 
# The second one is not putting the == sign. The third one is using else instead of elif. 

number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
elif number < 0:
    print("The number is negative.")