'''
Programmer Name: Joesph D. Aguilar
Description: This program determines user drink size and outputs drink order
Date: 07/29/2023
'''

#Project Instructions
'''
The Coffee vending machine provides coffee in three sizes: small (9oz), medium (12oz), and large (15oz).
Write a program to determine the drink size based on the letter the user enters. Print a message to the user 
giving the various drink size options and then prompt the user for the drink size. The user can enter an 's' or 'S' for small, 
an 'm' or 'M' for medium, and an 'l' or 'L' for large. Depending on which size the user requests, print a message such as: 
“You have ordered a (small, medium, large) drink.” In addition to displaying the size ordered, also record a price multiplier. 
The price multiplier for a small is 1, for a medium is 2, and for a large is3. If the user does not enter a valid character, 
print an error message (such as “Error: Invalid drink size”) and exit the program. You should use if-then-else statements for 
this problem. After the if-then-else statements, print the value of the price multiplier to ensure that the correct value was recorded 
(the price multiplier will be used in program 4). 
'''

#Coffee sizes
small = "Small Coffee (9oz)"
medium = "Medium Coffee (12oz)"
large = "Large Coffee (15oz)"

#Drink Multipliers
smSize = 1
medSize = 2
LgSize = 3
drinkSize = None

#User Values
userChoice = None

#Displaying Menu
print("Hello, Welcome to our Cafe Shop!")
print(f"Here is our coffee sizes: {small}, {medium}, and {large}. Which one would you like?")

userChoice = str(input("Enter you choice: "))
userChoice = userChoice.lower()

if (userChoice == 's' or userChoice == 'small'):
    drinkSize = smSize
    print(f'You have chosen the {small} drink.')
elif (userChoice == 'm' or userChoice == 'medium'):
    drinkSize = medSize
    print(f'You have chosen the {medium} drink.')
elif (userChoice == 'l' or userChoice == 'large'):
    drinkSize = LgSize
    print(f'You have chosen the {large} drink.')
else:
    print("Error: Invalid drink choice!")
    
print(f"Price Multiplier: {drinkSize}")