'''
Programmer Name: Joesph D. Aguilar
Description: This program displays drinks with prices and gets users order and outputs cost
Date: 07/29/2023
'''

#Program Instructions
'''
Write a program that displays the various coffee drinks your vending machine offers along with the option number for each drink. 
Beside each option include the price (you can set the cost for the small, the costs for medium should be 2 times the cost of the 
small and the cost of the large should be 3 times the cost of the small). These are some of the options you could choose from.

1.Espresso (Small $1.75 , Medium $3.50, Large $5.25)

2.Americano (Small $1.75 , Medium $3.50, Large $5.25)

3.Café au Lait (Small $1.75 , Medium $3.50, Large $5.25)

4.Latte (Small $1.75 , Medium $3.50, Large $5.25)

5.Cappuccino (Small $1.75 , Medium $3.50, Large $5.25)

6.Macchiato (Small $1.75 , Medium $3.50, Large $5.25)

7.Mocha (Small $1.75 , Medium $3.50, Large $5.25)

For example: Then prompt the user for their drink selection and enter their selection. Record the cost of the small drink into 
a variable that will be used to compute the amount due (to be used in program 4). Display a message such as “You selected Mocha ”. 
If the user does not enter a valid option, print an error message and exit the program. You should use a conditional statement for 
this problem. To check that you have recorded the amount due properly, after the statement, display the amount due for the small size 
of the drink selected. You must offer at least 4 drink options.
'''

#Vending Machine Items
itemOne = 'Espresso'
itemTwo = 'Americano'
itemThree = 'Latte'
itemFour = 'Mocha'

#Item Sizes
smallSize = "Small"
medSize = "Medium"
largeSize = "Large"

#Item Base Prices
itemOnePrice = 1.75
itemTwoPrice = 1.75
itemThreePrice = 1.75
itemFourPrice = 1.75

#Price Multipliers
small = 1
med = 2
large = 3

#User Values
userChoice = None
userDrink = None
userDrinkSize = None
total = None

#Displaying Menu
print("Welcome, Choose from the following:")
print(f'A.{itemOne.capitalize()}(Small ${itemOnePrice * small}, Medium ${itemOnePrice * med}, Large ${itemOnePrice * large})')
print(f'B.{itemTwo.capitalize()}(Small ${itemTwoPrice * small}, Medium ${itemTwoPrice * med}, Large ${itemTwoPrice * large})')
print(f'C.{itemThree.capitalize()}(Small ${itemThreePrice * small}, Medium ${itemThreePrice * med}, Large ${itemThreePrice * large})')
print(f'D.{itemFour.capitalize()}(Small ${itemFourPrice * small}, Medium ${itemFourPrice * med}, Large ${round(itemFourPrice * large, 2)})')

#Getting User Choice
userChoice = str(input('Choose your drink: '))
userChoice = userChoice.lower()

#Checking User Drink Choice
if (userChoice == 'a' or userChoice == itemOne):
    userDrink = itemOne
    total = itemOnePrice
    print(f'You choose {userDrink}, next choose your size.')
elif (userChoice == 'b' or userChoice == itemTwo):
    userDrink = itemTwo
    total = itemTwoPrice
    print(f'You choose {userDrink}, next choose your size.')
elif (userChoice == 'c' or userChoice == itemThree):
    userDrink = itemThree
    total = itemThreePrice
    print(f'You choose {userDrink}, next choose your size.')
elif (userChoice == 'd' or userChoice == itemFour):
    userDrink = itemFour
    total =itemFourPrice
    print(f'You choose {userDrink}, next choose your size.')
else:
    print('Error: Invalid drink choice!')
    
#Checking Drink Size
print(f'What size {userDrink} would you like: Small, Medium, or Large?')
userChoice = str(input("Choose your drink size: "))
userChoice = userChoice.lower()

#Validating Drink Size
if (userChoice == 's' or userChoice == 'small'):
    userDrinkSize= smallSize
    print(f'You have chosen: {userDrinkSize}')
elif (userChoice == 'm' or userChoice == 'medium'):
    userDrinkSize= medSize
    print(f'You have chosen: {userDrinkSize}')
elif (userChoice == 'l' or userChoice == 'large'):
    userDrinkSize= largeSize
    print(f'You have chosen: {userDrinkSize}')
else:
    print("Error: Invalid drink size!")
    
print(f'You chosen a {userDrink}, Price for a small is {total}')