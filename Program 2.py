'''
Programmer Name: Joesph D. Aguilar
Description: This program gets the users name and salary and calculates the federal/state tax
Date: 07/20/2023
'''

#Project Instructions
'''
Write a program to fetch the employee's name and salary.  Calculate the Federal tax and state tax based on the following criteria:
- If the salary is greater than 100000 then calculate the federal tax at 30% otherwise calculate the federal tax at 20%
- Calculate the state tax at 10%
- Calculate the net salary of the employee. To calculate the net salary, subtract federal and state tax from the gross salary.

'''

#Tax Variables
fedTax = 0.2 * 100
richTax = 0.3 * 100
stateTax = 0.1 * 100

#User Input Variables
userName = ''
userSalary = 0

#Total Variable
netSalary = 0

#Getting user values
while True:
    print("Please enter you first name")
    name = input()
    try:
        name = str(name)
    except:
        print("Please use letters only")
        continue
    if not name.isalpha():
        print("Name can't have numbers.")
        continue
    if len(name) <= 1:
        print("Name can't be one letter")
        continue
    break
userName = name

while True:
    print("What is your current salary?")
    salary = input()
    try:
        salary = float(salary)
    except:
        print("Please enter numeric digits")
        continue
    if salary < 1000.00:
        print("Please enter a valid salary")
        continue
    break
userSalary = salary

#Calculates and outputs values
if userSalary < 100000.00:
    netSalary = round(userSalary - fedTax - stateTax, 2)
    print(f'The net pay for {userName} is ${netSalary}, after 20% federal and 10% state tax.')
else:
    netSalary = round(userSalary - richTax - stateTax, 2)
    print(f'The net pay for {userName} is ${netSalary}, after 30% federal tax and 10% state tax. ')