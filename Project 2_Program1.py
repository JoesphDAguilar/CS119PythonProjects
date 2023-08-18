'''
Programmer Name: Joesph D. Aguilar
Description: This program will act as a coffee vending machine that collects money from user
Date: 07/29/2023
'''

#Project Instructions
'''

Write the money collection interface for the coffee vending machine. Your program should tell the user the 
price of the item and then the user will enter the amount of money that they are paying (this simulates them 
actually inserting cash). If the money collected is less than the price, print an appropriate message (such as: “Insufficient funds, no sale!”) and then the program should exit.

If enough money is collected, determine the amount to return to the customer. If the change due is not zero, 
tell the user how much change they will receive. Next print a message (such as “Thank you - enjoy your coffee !”) and end the program normally.

Note, your program should be able to handle all amounts of money (not just multiples of dollars but also cents such as $1.25). 
Also you may assume that the user is only entering a number and not the $ (though the $ could be part of your prompt).
Hint: Check how to do floating point comparisons!

'''


#Vending Selection
itemOne = "coffee"
itemTwo = "coco"
itemThree = "milk"
itemFour = "water"

#Vending Prices
itemOnePrice = 1.50
itemTwoPrice = 1.25
itemThreePrice = 1.10
itemFourPrice = 1.00

#User Values
userChoice = None
userTotal = None
userMoney = None
userChange = None

#Getting User Selection

while True:
    print(f"Welcome, we have Coffee $1.50, Coco 1.25, Milk $1.10 or Water for $1.00")
    vendor = input("What will you be having today: ")
    try:
        userChoice = str(vendor.lower())
        if (userChoice == itemOne or userChoice == itemTwo or userChoice == itemThree or userChoice == itemFour):
            break
        else:
            print("Please enter a valid drink")
    except ValueError:
        print("Error: Please enter letters only.")
    
#Comparing User Choice
if (userChoice == itemOne):
    userTotal = itemOnePrice
    print(f"Your total is: ${itemOnePrice}")
elif (userChoice == itemTwo):
    userTotal = itemTwoPrice
    print(f"Your total is: ${itemTwoPrice}")
elif (userChoice == itemThree):
    userTotal = itemThreePrice
    print(f"Your total is: ${itemThreePrice}")
else:
    userTotal = itemFourPrice
    print(f"Your total is: ${itemFourPrice}")
    
while True:
    print("Please enter your amount of money you will be paying with: ")
    money = input("Enter Amount: ")
    try:
        money = float(money)
        if (money >= userTotal):
            userMoney = money
            break
        else:
            print("Please enter more money to cover total.")
    except ValueError:
        print("Please use numerical digits only.")
    

userChange = round(userMoney - userTotal, 2)
print(f'Your change is ${userChange}')