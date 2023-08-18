'''
Programmer Name: Joesph D. Aguilar
Description: This program displays a menu to allow the user to add, insert, remove, find the maximum, the minimum, and sort the list in descending order 
Date: 08/14/2023
'''

#Project Instructions

'''
For this program, you have to write your own functions for lists without using any of the build-in functions. 
Create a menu to allow the user to add, insert, remove, find the maximum, the minimum, and sort the list in 
descending order (larger to smaller value). You are allowed to only use len(), and index()

studentFullName=["Mike navarro","Miguel saba","Maria Rami"]

You may only use these build in functions len(), index(). Here is an sample output:

1- Add an item to the list  ..........addItem(item) 
2- Remove item from the list .......removeItem(item)
3- Insert an item to the list .....insertToList(item, index)
4- Find maximum ....findMax(list)
5- Find Minimum ....findMax(list)
6- Sort the list in descending order .....sortList(list)
7- Display the list.... displayList(list)
8- Quit the program .....exit()
Please enter your option: 3 

Where do you want to insert the item? (Enter the index number) 1
Please enter the value for the item you want to insert: "Tina Mari"
Your program should call the function  insertToList(item, index)
Your original List : ["Mike navarro","Miguel saba","Maria Rami"]
After inserting an item into index 1:
["Mike navarro","Tina Mari", "Miguel saba","Maria Rami"]

Once the user enters an option, your program should execute the code for that option and displays the list before and 
after the operations. Make sure to use a while loop so the program runs until user enters the quit option.

'''

#Start of Code

'''
Variables
'''

colorsList = ['purple', 'green', 'orange', 'yellow']
choice = None
repeat = None
start = 1
end = 2
'''
Functions
'''

#Displays the menu options and gets user's choice
def menuOptions():
    print('1- Add an item to the list')
    print('2- Remove item from the list')
    print('3- Insert an item to the list')
    print('4- Find maximum')
    print('5- Find minimum')
    print('6- Sort the list in descending order')
    print('7- Display the list')
    print('8- Quit the program')
    
    while True:
        try:
            userChoice = int(input('\nPlease enter your option: '))
            
            if userChoice > 0 and userChoice <= 7:
                return userChoice
            if userChoice == 8:
                 exit()
                 return userChoice 
        except ValueError:
            print('Error: Please choose an option from 1 to 8.')
            continue
        
#Adds an item to list
def addItem():
    while True:
        item = str(input('Enter an item to add: '))
        
        if isinstance(item,str):
            return colorsList.append(item)
        else:
            print('Error: Please enter letters only!')
            continue

#Removes an item from list
def removeItem():
    while True:
        item = str(input('Enter an item to remove: '))
        
        if isinstance(item, str):
            if item in colorsList:
                return colorsList.remove(item)
            else:
                print('Error: Please enter a valid item!')
        else:
            print('Error: Please enter letters and an item in the list only!')
            continue
        
#Inserts an item to list
def insertToList():
    while True:
        try:
            index = int(input('Where do you want to insert the item?(Enter the index): '))
            item = input('Please enter the value for the item you want to insert:  ')
            if 0 <= index < len(colorsList):
                    return colorsList.insert(index, item)
            else:
                print("Error: Please enter a valid index!")
        except ValueError:
            print("Error: Please use numbers only!")
            continue
        
#Find the max value of list
def findMax(list):
    maxValue = None
    
    for value in list:
        if maxValue is None or len(value) > len(maxValue):
            maxValue = value
            
    return (f'The max value is: {maxValue}')
        
#Finds the min value of list
def findMin(list):
    minValue = None
    
    for value in list:
        if minValue is None or len(value) < len(minValue):
            minValue = value
            
    return (f'The min value is: {minValue}')      

#Sorts the List in descending order
def sortList(list):
    descendList = sorted(list)
    return descendList

#Displays current list
def displayList(list):
    print(f'Current list: {list}')

#exits the program
def exit():
    print('Goodbye! Ending Program...')
    
    

'''
Main Code
'''

#Runs till user enters no at end of each choice
while start < end and choice != 8:
    choice = menuOptions()
    
    #Choice 1
    if choice == 1:
        print(f'Original list: {colorsList}')
        addItem()
        print(f'After adding to list: {colorsList}')
        while True:
            repeat = input('\nDid you want to continue (yes or no): ')
            if repeat == 'yes':
                start = 1
                print('Continuing...\n')
                break
            elif repeat == 'no':
                start = 2
                exit()
                break
            else:
                print('Error: Please enter yes or no only. (case sensitive)')
                continue
    
    #Choice 2
    if choice == 2:
        print(f'Original list: {colorsList}')
        removeItem()
        print(f'After removing item from list: {colorsList}')
        while True:
            repeat = input('\nDid you want to continue (yes or no): ')
            if repeat == 'yes':
                start = 1
                print('Continuing...\n')
                break
            elif repeat == 'no':
                start = 2
                exit()
                break
            else:
                print('Error: Please enter yes or no only. (case sensitive)')
                continue

    #Choice 3
    if choice == 3:
        print(f'Original list: {colorsList}')
        insertToList()
        print(f'After adding item to index: {colorsList}')
        while True:
            repeat = input('\nDid you want to continue (yes or no): ')
            if repeat == 'yes':
                print('Continuing...\n')
                start = 1
                break
            elif repeat == 'no':
                start = 2
                exit()
                break
            else:
                print('Error: Please enter yes or no only. (case sensitive)')
                continue
    
    #Choice 4
    if choice == 4:
        print(f'List: {colorsList}')
        print(findMax(colorsList))
        while True:
            repeat = input('\nDid you want to continue (yes or no): ')
            if repeat == 'yes':
                print('Continuing...\n')
                start = 1
                break
            elif repeat == 'no':
                start = 2
                exit()
                break
            else:
                print('Error: Please enter yes or no only. (case sensitive)')
                continue
    
    #Choice 5
    if choice == 5:
        print(f'List: {colorsList}')
        print(findMin(colorsList))
        while True:
            repeat = input('\nDid you want to continue (yes or no): ')
            if repeat == 'yes':
                print('Continuing...\n')
                start = 1
                break
            elif repeat == 'no':
                start = 2
                exit()
                break
            else:
                print('Error: Please enter yes or no only. (case sensitive)')
                continue

    #Choice 6
    if choice == 6:
        print(f'List: {colorsList}')
        print(f'List in descending order: {sortList(colorsList)}')
        while True:
            repeat = input('\nDid you want to continue (yes or no): ')
            if repeat == 'yes':
                print('Continuing...\n')
                start = 1
                break
            elif repeat == 'no':
                start = 2
                exit()
                break
            else:
                print('Error: Please enter yes or no only. (case sensitive)')
                continue
    
    #Choice 7
    if choice == 7:
        displayList(colorsList)
        while True:
            repeat = input('\nDid you want to continue (yes or no): ')
            if repeat == 'yes':
                print('Continuing...\n')
                start = 1
                break
            elif repeat == 'no':
                start = 2
                exit()
                break
            else:
                print('Error: Please enter yes or no only. (case sensitive)')
                continue
            
 #End of code   
