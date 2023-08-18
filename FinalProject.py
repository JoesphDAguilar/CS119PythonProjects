'''
Programmer Name: Joesph D. Aguilar
Description: Program simulates a banking app that reads a username, password and balances for each customer
Date: 8/16/2023
'''

#Program Instruction

'''

You are going to write a program called BankApp to simulate a banking application.
The information needed for this project are stored in a text file. Those are:
usernames, passwords, and balances.

Your program should read username, passwords, and balances for each customer, and
store them into three lists.

userName (string), passWord(string), balances(float)

The txt file with information is provided as UserInformtion.txt

Example: This will demonstrate if file only contains information of 3 customers. You
could add more users into the file.
userName passWord Balance
========================
Mike sorat1237# 350
Jane para432@4 400
Steve asora8731% 500

When a user runs your program, it should ask for the username and password
first. Check if the user matches a customer in the bank with the information
provided. Remember username and password should be case sensitive.

After asking for the user name, and password display a menu with the following
options and ask the user for input (Use a While Loop).

Type D to deposit money
Type W to withdraw money
Type B to display Balance
Type C to change user, display user name
Type A to add new client
Type E to exit

If the user types D
(Deposit Function) Ask the user to enter the amount to deposit.
Then call the Deposit Function, passing the deposit amount as a parameter. The
function should update the Balance.
Then display the new balance (this should happen by calling the ShowBalance
function).
Then display the menu again

If the user types W
(Withdraw Function) Ask the user to enter the amount he/she wants to withdraw.
Before calling the withdraw function, make sure there is enough balance. Call
the ShowBalance function before Withdraw function!!
Then call the Withdraw Function, passing the withdraw amount as a parameter.
The function should update the Balance.
Display the new balance to the user.
Then display the menu again

If the user enters B
(ShowBalance Function)
Display the Balance.

If the user enters C
(ChangeUser Function) Ask for the user name and change to a different
customer.

If the user enters A 
(AddNewUser function) Ask for username, password,and balance. These information 
will be added to the appropriate lists which
later on will be transferred to the UserInformation.txt

If the user types any other option: Prompt the user that option is invalid

If the user types E then
Terminate the program and update the UserInformtion.txt with the correct
updated balances.

PS: You program must keep displaying the menu until the user types the option
E, to exit the program.

'''


'''
Variables
'''
#List Variables
userName = ['mike', 'jane', 'steve']
passWord = ['sorat1237#', 'para432@4', 'asora8731%']
balances = [350.0, 400.0, 500.0]

#User Variables
currentUser = None
currentUserIndex = None
userPass = None
userBalance = None
userChoice = None
updatedBalance = None
newName = None
newPass = None
newBalance = None

#Menu variables
deposit = None
withdraw = None

#Main Loop Variables
start = 1
end = 2

'''
Functions
'''
#Welcome Message
def welcome():
    print('Welcome to World Bank, Please enter you login information to access your account.')
    
def menu():
    print('\nType D to deposit money')
    print('Type W to withdraw money')
    print('Type B to display balance')
    print('Type C to change user')
    print('Type A to add new client')
    print('Type E to exit')

#Gets index of user
def getUserIndex(user, userList):
    for i in range(len(userList)):
        if userList[i] == user:
            return userList.index(user)


#Validates if user input is in a list and returns the value 
def getUser(userList):
    while True:
        try:
            loginName = str(input('Username: ')).lower()
            
            if loginName in userList:
                for i in range(len(userList)):
                    if userList[i] == loginName:
                        return loginName
                
            elif not loginName in userName:
                print('Error: Username not found! Please enter a valid username.')
                continue
        except ValueError:
            print('Error: Please use letters only!')

            

#Takes an index and a list as parameters and iterates through list. Returns value of that index
def getBalance(index, balance):
    for i in range(len(balance)):
        return balance[index]


              
#Gets the user's password and validates if it belongs to the current user
def getPass(passList, userIndex):
    while True: 
        try:
            userPass = str(input('Password: '))
            
            if userPass in passList:
                passCheck = passList.index(userPass)
                if passCheck == userIndex:
                    return True
            else:
                print("Error: Please enter a valid password!")
        except ValueError:
                print('Error: Please use valid characters!')
                continue
               
            
#Deposit function
def userDeposit():
    while True:
        try:
            amount = float(input('Enter deposit amount: $'))
            userAmount = round(amount, 2)
            return userAmount
        except ValueError:
            print('Error: Please enter digits only!')


#Withdraw function
def userWithdraw():
    while True:
        try:
            amount = float(input('Enter withdraw amount: $'))
            userAmount = round(amount, 2)
            return userAmount
        except ValueError:
            print('Error: Please enter digits only!')
         

#Calls functions: getUser, getUserIndex, and getPass to change user
def changeUser():
    print('\nEnter username that you would like to switch to.\n')
    

#Displays all user names
def displayNames(nameList):
    for i in range(len(nameList)):
        print(nameList[i].capitalize())  
    
    

#Updates list and adds new user information
def addNewUser(userInfo, userList):
    userList.append(userInfo)


#Goodbye message
def exit():
    print('Goodbye! Ending Program...')
    

#Updates balance in txt file
def updateBalanceFile(oldBal, newBal):
    
    oldBal = str(round(oldBal))
    newBal = str(round(newBal))
    
    
    fin = open('UserInformtion.txt', 'rt')
    data = fin.read()
    data = data.replace(oldBal, newBal)
    fin.close

    fin = open('UserInformtion.txt', 'wt')
    fin.write(data)
    fin.close()
    
    print('Balance updated in UserInformtion.txt')

'''
Main Code
'''

#Calling functions to start program
welcome()
currentUser = getUser(userName)
currentUserIndex = getUserIndex(currentUser, userName)
userPass = getPass(passWord, currentUserIndex)  
menu()

#User Input check
while start < end:
    userChoice = str(input('\nEnter Choice: ')).lower()
    
    #Deposit
    if userChoice == 'd':
        deposit = userDeposit()
        userBalance = getBalance(currentUserIndex, balances)
        updatedBalance = userBalance + deposit
        print(f'Balance: {updatedBalance}')
        while True:
            repeat = input('\nDid you want to continue (y/n): ')
            if repeat == 'y':
                print('Continuing...\n')
                menu()
                start = 1
                break
            elif repeat == 'n':
                start = 2
                exit()
                updateBalanceFile(userBalance, updatedBalance)
                break
            else:
                print('Error: Please enter y or n only. (case sensitive)')
                continue
        
    #Withdraw
    if userChoice == 'w':
        withdraw = userWithdraw()
        userBalance = getBalance(currentUserIndex, balances)
        updatedBalance = userBalance - withdraw
        print(f'Balance: {updatedBalance}')
        while True:
            repeat = input('\nDid you want to continue (y/n): ')
            if repeat == 'y':
                print('Continuing...\n')
                menu()
                start = 1
                break
            elif repeat == 'n':
                start = 2
                exit()
                updateBalanceFile(userBalance, updatedBalance)
                break
            else:
                print('Error: Please enter y or n only. (case sensitive)')
                continue
            
    #Display Balance
    if userChoice == 'b':
        userBalance = getBalance(currentUserIndex, balances)
        print(f'Current Balance: ${userBalance:g}')
        while True:
            repeat = input('\nDid you want to continue (y/n): ')
            if repeat == 'y':
                print('Continuing...\n')
                menu()
                start = 1
                break
            elif repeat == 'n':
                start = 2
                exit()
                break
            else:
                print('Error: Please enter y or n only. (case sensitive)')
                continue
    
    #Change User
    if userChoice == 'c':
        changeUser()
        print('Available users:')
        displayNames(userName)
        print('\n')
        currentUser = getUser(userName)
        currentUserIndex = getUserIndex(currentUser, userName)
        print(f'Welcome {currentUser.capitalize()}, Please enter your password.')
        userPass = getPass(passWord, currentUserIndex)
        while True:
            repeat = input('\nDid you want to continue (y/n): ')
            if repeat == 'y':
                print('Continuing...\n')
                menu()
                start = 1
                break
            elif repeat == 'n':
                start = 2
                exit()
                break
            else:
                print('Error: Please enter y or n only. (case sensitive)')
                continue 
    
    #Add user
    if userChoice == 'a':
        while True:
            newName = input('Enter username for new user: ').lower()
            
            if not len(newName) == 0 and not newName.isspace() and not newName.isdigit():
                addNewUser(newName, userName)
                break
            else:
                print("Error: Please don't leave blank and use letters only!")
                continue
        
        while True:
            newPass = input('Enter your password for new user: ')
            
            if not len(newPass) < 3 and not newPass.isspace():
                addNewUser(newPass, passWord)
                break
            else:
                print('Error: Password must be at least 3 characters without spaces!')
                continue
        
        while True:
            try:
                newBalance = float(input('Enter balance for new user: '))
                
                if newBalance >= 0:
                    newBalance = round(newBalance, 2)
                    addNewUser(newBalance, balances)
                    break
                else:
                    print('Error: Balance must be zero or more!')
                    continue
            except ValueError:
                print('Error: Please enter a valid balance using numbers only.')
                continue
        
        while True:
            repeat = input('\nDid you want to continue (y/n): ')
            if repeat == 'y':
                print('Continuing...\n')
                menu()
                start = 1
                break
            elif repeat == 'n':
                start = 2
                exit()
                break
            else:
                print('Error: Please enter y or n only. (case sensitive)')
                continue 
    

    #Exit
    if userChoice == 'e':
        exit()
        start = 2
                
            
             
        
        