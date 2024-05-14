'''
This is a note for Module 2 of Python Basics. 
This is a Multi-line String comment. 

LESSON 2: Python Conditional Statement
'''

# The "if, elif, else" statement

#Example

red_potion = True
blue_potion = False

if red_potion and not blue_potion:
    print("You get a potion of strength!")
elif not red_potion and blue_potion:
    print("You get a potion of speed!")
elif red_potion and blue_potion:
    print("Oops! Mixing red and blue makes it explode!")
else:
    print("No potion was mixed.")

#Exercise 2 : Movie Age Restriction

movie_rating = "PG-13"
age_p = 14

if(age_p > 13):
    print("You can watch a PG-13 movie including G and PG however R is forbidden.")
else:
    print("You are not in the age range to watch this movie. Please try G or PG.")


#From video
print("")

age = int(input("Enter your age: "))
rating = input("Enter movie rating (G, PG, pg-13, R): ")

if rating == "G":
    print("You can watch this movie!")
elif rating == "PG" and age >= 7:
     print("You can watch this movie!")
elif rating == "PG-13" and age >= 13:
     print("You can watch this movie!")
elif rating == "R" and age >= 17:
     print("You can watch this movie!")
else:
     print("You are not allowed to watch this movie")
