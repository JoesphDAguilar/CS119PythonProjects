'''
Programmer Name: Joesph D. Aguilar
Description: Computes and displays the charges for a patient's hospital stay.
Date: 08/14/2023
'''

#Project Instruction

'''

Write a program that computes and displays the charges for a patient's hospital stay. 
First, the program should ask if the patient was admitted as an in-patient or an out-patient. If the
patient was an in-patient the following data should be entered:
• The number of days spent in the hospital
• The daily rate
• Charges for hospital services (lab tests, etc.)
• Hospital medication charges.

If the patient was an out-patient the following data should be entered:
• Charges for hospital services (lab tests, etc.)
• Hospital medication charges.

Use a single, separate function to validate that no input is less than zero. If it is, it should
be re-entered before being returned. Once the required data has been input and validated, the program should use two
separate functions to calculate the total charges. One of the functions should accept arguments for the in-patient data, 
while the other function accepts arguments for out-patient data. Both functions should return the total charges.

'''

#Variables:
patient = None
days = None
rate = None
services = None
medsCost = None


#Defining function:

#Checks if user is in or out patient and stores it in a variable
def inOutPatientCheck():
    while True:
        check = input('Are you an in-patient or an out-patient? Enter in for in-patient or out for out-patient: ').lower()
        
        if check == 'in':
            patient = check
            return patient
        elif check == 'out':
            patient = check
            return patient
        else:
            print('Error: Enter in or out only!')
      
patient = inOutPatientCheck()

#Checks if user input is valid, if valid returns true if not returns false
def checkValue(value):
    if value is None or value < 0:
        return False
    
    allowedType = (int, float)
    
    if not isinstance(value, allowedType):
        return False
    
    return True


#In=patient calculator; w for days, x for daily rate, d for services and z for medication charges
def inCal(w, x, y, z):
    total = round((w * x) + y + z, 2)
    print(f'\nNumber of days spent in hospital: {w}')
    print(f'Daily rate: ${format(x,".2f")}')
    print(f'Charges for hospital services: ${format(y,".2f")}')
    print(f'Charges for hospital medication: ${format(z,".2f")}')
    print(f'Your in-patient total: ${format(total,".2f")}')
    
    
#Out-patient calculator; x for hospital services and y for hospital medication charges
def outCal(x, y):
    total = round(x + y, 2)
    print(f'\nCharges for hospital services: ${format(x,".2f")}')
    print(f'Charges for hospital medication: ${format(y,".2f")}')
    print(f'Your out-patient total: ${format(total,".2f")}')


#Main code:

#Runs if user is an in-patient 
if patient == 'in':
  while True:
      try:
          userDays = int(input('Please enter number of days spent in hospital: '))
          userDayCheck = checkValue(userDays)
          
          if userDayCheck is True:
              days = userDays
          else:
              print("Please enter a number 0 or more.")
              continue  
      except ValueError:
          print('Error: Please enter a valid number of days!')
          
      try:
          userRate = float(input('Please enter the daily rate: '))
          userRateCheck = checkValue(userRate)
          
          if userRateCheck is True:
              rate = userRate   
          else:
              print("Please enter a number 0 or more.")
              continue  
      except ValueError:
          print('Error: Please enter a valid daily rate!')
          
      try:
          userServices = float(input('Please enter charges for hospital services(lab test etc.): '))
          userServicesCheck = checkValue(userServices)
          
          if userServicesCheck is True:
              services = userServices
              
          else:
              print("Please enter a number 0 or more.")
              continue  
      except ValueError:
          print('Error: Enter a valid total for hospital services!')
        
        
      try:
          userMeds = float(input('Please enter charge for hospital medication: '))
          userMedsCheck = checkValue(userMeds)
         
          if userMedsCheck is True:
             medsCost = userMeds
             inCal(days, rate, services, medsCost)
             break
          else:
             print('Please enter a number 0 or more.')
      except ValueError:
          print('Error please enter a valid total for hospital medication.')
        

#Runs if user is an out-patient
if patient == 'out':
    while True:
        try:
          userServices = float(input('Please enter charges for hospital services(lab test etc.): '))
          userServicesCheck = checkValue(userServices)
          
          if userServicesCheck is True:
              services = userServices
              
          else:
              print("Please enter a number 0 or more.")
              continue  
        except ValueError:
          print('Error: Enter a valid total for hospital services!')
        
        try:
          userMeds = float(input('Please enter charge for hospital medication: '))
          userMedsCheck = checkValue(userMeds)
         
          if userMedsCheck is True:
             medsCost = userMeds
             outCal(services, medsCost)
             break
          else:
             print('Please enter a number 0 or more.')
        except ValueError:
          print('Error please enter a valid total for hospital medication.')


   