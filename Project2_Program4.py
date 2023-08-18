'''
Programmer Name: Joesph D. Aguilar
Description: This program acts like a virtual vending machine and outputs user order 
Date: 07/29/2023
'''

#Project Instructions
'''
Write a program that combines programs 1 through 3 into one vending machine user interface program. 
First welcome the user and display the drink options, prompt the user for their drink selection, enter 
their selection, and record the amount due for a small (program 3).

Next, display the size options, prompt the user for the size, enter their size selection, and record the 
price multiplier (program 2). Based on the size entered, your program should adjust the amount due. Next, 
display the amount due, prompt the user for their payment, enter their payment, and determine the amount of change to return (program 1).

Note: Any additional computations or control should also be included. In program 4 you should remove any 
unnecessary print statements used in programs 1 through 3 that do not display useful information to the user.
'''

#Vending Display Options
itemOne = "Espresso"
itemTwo = "Americano"
itemThree = "Latte"
itemFour = "Mocha"

#Size Options
smSize = "small"
medSize = "medium"
lgSize = "large"

#Size Multipliers
sm = 1
med = 2
lg = 3

#Vending Prices
aPrice = 1.75
bPrice = 1.75
cPrice = 1.75
dPrice = 1.75

#User Values
userChoice = None
userDrink = None
userDrinkSize = None
userTotal = None
userMoney = None
userChange = None

#Welcome Message and Menu Display
print("Hello and Welcome, Please make a selection from our menu:")
print(f"A.{itemOne.capitalize()}(Small ${aPrice * sm}, Medium ${aPrice * med}, Large ${round(aPrice * lg, 2)})")
print(f"B.{itemTwo.capitalize()}(Small ${bPrice * sm}, Medium ${bPrice * med}, Large ${bPrice * lg})")
print(f"C.{itemThree.capitalize()}(Small ${cPrice * sm}, Medium ${cPrice * med}, Large ${cPrice * lg})")
print(f"D.{itemFour.capitalize()}(Small ${dPrice * sm}, Medium ${dPrice * med}, Large ${round(dPrice * lg, 2)})")

#Getting User Drink Choice
while True:
    print("\nPlease choose your drink of choice:")
    vendor = input('Drink choice: ')
    try:
        userChoice = str(vendor.lower())
        if (userChoice == itemOne):
            userDrink = itemOne
            userTotal = aPrice
            break
        elif (userChoice == itemTwo):
            userDrink = itemTwo
            userTotal = bPrice
            break
        elif (userChoice == itemThree):
            userDrink = itemThree
            userTotal = cPrice
            break
        elif (userChoice == itemFour):
            userDrink = itemFour
            userTotal = dPrice
            break
        else:
            print("Error! Please enter a valid drink choice.")
    except ValueError:
        print('Please enter a valid drink using letters only.')
        
#Loop Output test
print(f'You choose {userDrink}, A small cost {userTotal}. Lets get your drink size next.\n')

#Getting User Drink Size
while True:
    print("Choose your drink size: Small, Medium, or Large.")
    size = input("Enter your drink size: ")
    try:
        userChoice = str(size.lower())
        if (userChoice == 's' or userChoice == smSize):
            userDrinkSize = smSize
            userTotal = userTotal * sm
            break
        elif (userChoice == 'm' or userChoice == medSize):
            userDrinkSize = medSize
            userTotal = userTotal * med
            break
        elif (userChoice == 'l' or userChoice == lgSize):
            userDrinkSize =lgSize
            userTotal = round(userTotal * lg, 2)
            break
        else:
            print('Please enter Small, Medium, or Large only.')
    except ValueError:
        print("Error! Please enter letters only")

#Drink Size Loop Test
print(f'You chose the size {userDrinkSize}, your total is {userTotal}. Lets put it all together now.\n')

#Getting User Money And Giving Change
print(f'You have chosen a {userDrinkSize} {userDrink}, Your total is ${userTotal}.')

while True:
    print('How much money will you be paying with?')
    money = input()
    try:
        userMoney = float(money)
        if (userMoney > userTotal):
            userChange = round((userMoney - userTotal), 2)
            print(f'Your change is ${userChange}. Thank you and enjoy the rest of your day!')
            break
        elif (userMoney == userTotal):
            userChange = userMoney - userTotal
            print('You payed the exact amount, No change given. Thank you ane a great day!')
            break
        else: 
            print('Please add more money to cover your total!')
    except ValueError:
        print('Please enter numerical digits only!')