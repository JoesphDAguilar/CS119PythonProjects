'''
Programmer Name: Joesph D. Aguilar
Description: Calculates and prints bill for a cellphone company
Date: 07/21/20023
'''

#Program Instruction
'''

You will write a program that calculates and prints the bill for a cellular telephone company.
A telephone company offers two types of service: regular and premium. Its rate varies, depending on the type of service. The rates are compared as follows.

Regular service:    $10.00 plus the first 50 minutes are free. Charges for over 50 minutes are $0.20 per minute.

Premium service:  $25 plus:
* For calls made from 6:00 a.m. to 6:00 p.m., the first 75 minutes are free; charges for more than 75 minutes are $0.10 per minute
* For calls made from 6:00 pm to 6:00 a.m., the first 100 minutes are free; charges for more than 100 minutes are $0.05 per minute.

Your program should prompt the user to enter an account number, a service code (type character), and the number of minutes the service was used. 
A service code of r or R means regular service; a service code of p or P means premium service. Treat any other character as an error. Your program 
should output the account number, type of service, number of minutes the telephone service was used, and the amount due from the user.

For the premium service, the customer may be using the service during the day and the night. Therefore, to calculate the bill, you must ask the user 
to input the number of minutes the service was used during the day and the number of minutes the service was used during the night.

'''

#Rates variables
regRate = 10.00
regExtra = 0.20
premRate = 25.00
premExtraAm = 0.10
premExtraPm = 0.05

#premium rate variables
dayMins = None
nightMins = None
dayTotal = None
nightTotal = None

#User input variables
userAccount = None
userCode = None
userMins = None
userDayMins = None
userNightMins = None
userTotal = None
remMins = None

#Confirmation message function
def confirm():
    print("\nThank you, Moving on: ")
    
#User output function
def userInfo():
    print(f'\nAccount Number: {userAccount}')
    
    if userCode == 'r':
        print(f'Service Type: Regular')
    else:
        print('Service Type: Premium')
             
    print(f'Number of minutes used: {userMins}')
    print(f'Unaccounted for minutes: {remMins}')
    print(f'Your total for this month is: ${userTotal:.2f}')

#Getting user account number
while True:
    print("Please enter your account number: ")
    account = input()
    
    try:
        account = int(account)
    except:
        print("Please enter numeric digits.")
        continue
    if account <= 2:
        print("Please enter a positive number that is more than 2 digits. ")
        continue
    break
userAccount = account

confirm()

#Getting user service code
while True:
    print("Please enter your service code: R(regular service) or P(Premium Service)")
    serviceCode = input()
    
    try:
        serviceCode = str(serviceCode)
        serviceCode = serviceCode.lower()
    except:
        if not serviceCode.isalpha():
            print('Please do not use numbers.')
            continue
        if serviceCode != 'r' or serviceCode != 'p':
            print('Please enter your service code.')
            continue
    break
userCode = serviceCode

confirm()

#Getting user mins
while True:
    print("Please enter the number of minutes of service you have used: ")
    serviceMins = input()
    
    try:
        serviceMins = int(serviceMins)
        if serviceMins > 0:
            break
        else: 
            print("Please enter a number greater than 0.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
userMins = serviceMins

confirm()
print("\nCalculating...")

if userCode == 'r':
    if (userMins - 50) > 50:
        userTotal = (userMins * regExtra) + regRate
        userInfo()
    else:
        userTotal = regRate
        userInfo()
else:
    while True:
        print("\nPlease enter number of minutes used during the day (6:00am - 6:00pm): ")
        dayMins = input()
        
        print("\nPlease enter number of minutes used during the night (6:00pm - 6:00am): ")
        nightMins = input()
        try:
            dayMins = int(dayMins)
            nightMins = int(nightMins)
            if dayMins >= 0 and nightMins >=0:
                break
            else:
                print("Please enter a positive number")
        except ValueError:
            print('Invalid input. Please enter a valid number')
    userDayMins = dayMins
    userNightMins = nightMins
    if (userDayMins - 75) > 75:
        dayTotal = userDayMins * premExtraAm
    if(userNightMins - 100) > 100:
        nightTotal = userNightMins * premExtraPm
        userTotal = premRate + dayTotal + nightTotal
        remMins = userMins % (userDayMins + userNightMins) 
        userInfo()
    else:
        userTotal = premRate
        remMins = userMins % (userDayMins + userNightMins) 
        userInfo()
