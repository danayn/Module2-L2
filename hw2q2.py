'''
2. Quick Decisions: The Event Planner 🎉
Objective:
To practice the use of shorthand if statements in determining event-related decisions.


Task 1: Code Correction *
You are provided with a Python script that is supposed to help in event planning, but it has errors. Identify and fix them.


Task 2: Venue Selection *
Based on the corrected code from Task 1, further enhance the program to recommend additional facilities 
like "audio system" or "projector" based on the number of attendees.


Task 3: Catering Choices *
Ask the user if they want "vegetarian" food. Recommend "Veggie Delight Caterers" 
if yes, otherwise recommend "Gourmet Meals Caterers".
'''

#Task 1: Code Correction
attendees = int(input("Enter number of attendees: "))
if attendees > 100 :
   venue = "large hall" 
#Task 2: Venue Selection
   if attendees > 120:
      venue = venue + " and audio system"
   if attendees > 200:
      venue = venue + " and also a projector"
else:
   venue = "conference room"
 
print(venue)

#Task 3: Catering Choices
food = input("say 'yes' if you want vegetarian food: ")
if food == "yes":
   print("Veggie Delight Caterers recommended for vegetarians.")
else:
   print("Gourmet Meal Caterers recommended for non-vegetarians.")