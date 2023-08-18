'''
Programmer Name: Joesph D. Aguilar
Description: Displays a menu and lets user add, remove and display new menu as well as show min and max
Date: 08/07/2023
'''

#Project Instructions

'''

Create a menu to allow the user to add, insert, remove, find the maximum, the minimum, and sort the list 
in descending order (larger to a smaller value). Declare your list as a list of strings.

studentFullName=["Mike navarro","Miguel saba","Maria Rami"]

You may use any of the build-in functions. Here is a sample output:

1- Add an item to the list
2- Remove an item from the list ==> Ask for the name not the index for removal 
3- Insert an item into the list
4- Find maximum
5- Find the Minimum
6- Sort the list in descending order
7- Quit the program

Please enter your option: 3
Where do you want to insert the item? (Enter the index number) 1
Please enter the value for the item you want to insert: "Tina Mari"
Your original List : ["Mike navarro","Miguel saba","Maria Rami"]
After inserting an item into index 1:
["Mike navarro","Tina Mari", "Miguel saba","Maria Rami"]

Once the user enters an option, your program should execute the code for that option and displays the list before and after the operations.
Make sure to use a while loop so the program runs until the user enters the quit option.

'''

#Variables
menu = ['hot dog', 'hamburger', 'pizza', 'chicken']
maxItem = max(menu, key=len)
minItem = min(menu, key=len)
descOrder = sorted(menu, key=len)
userNum = None
userItem = None
repeat = 0
x = 100

#Ask to display menu for user or exits program
while True:
    print('Would you like to look at the menu?')
    userChoice = input("Yes or No: ").lower()
    
    if userChoice == 'yes':
        print("Menu: ")
        for item in menu: 
            print(item)
        break
    elif userChoice == 'no':
        print('Exiting program...Goodbye!')
        break
    else:
        print("Error: Please enter yes or no.")

#Loop runs at least once to 100 times, will end if user inputs no at end of loop 
#Gets the user inputs, checks if each input is valid for each prompt 
for repeat in range(x):
    if userChoice == 'no':
        break
        
    while True:
        print("What item would you like to add to the list?")
        userItem = input('Item: ').lower()
        
        if not userItem.isdigit():
            break
        else:
            print('Error: Please enter letters only.')
        
    while True:
        try: 
            print('Where would you like to add to the list(Please enter index number): ')
            userNum = int(input('Index number: '))
            print(f"Menu before: {menu}")
            menu.insert(userNum, userItem)
            print(f'Menu after: {menu}')
            break
        except ValueError:
            print('Error: Please enter a number only!')
        except IndexError:
            print('Error: Please enter a valid index number')
            
    while True:
            print('Enter a menu item to remove from the current menu.')
            removeItem = input('Remove item: ').lower()
            
            if not removeItem.isdigit():
                if removeItem in menu:
                    print(f'Menu before: {menu}')
                    menu.remove(removeItem)
                    print(f'Menu after: {menu}')
                    print(f'Menu item with max value: {maxItem}')
                    print(f'Menu item with min value: {minItem}')
                    print(f'Menu sorted in descending order: {descOrder}')
                    break
                else:
                    print(f'Error: {removeItem} is not in the list!')
            else:
                print('Error: Please enter letters only!')
                
    while True:              
        print('Would you like to repeat the process?')
        userChoice = input('Yes or No: ').lower()
        
        if userChoice == 'yes':
            print('Continuing...')
            break
        elif userChoice == 'no':
            print('Goodbye!')
            x = 0
            break
        else:
            print('Error: Please enter Yes or No!')
            