'''
Programmer Name: Joesph D. Aguilar
Description: Program  calculates yearly salary of 5 people and displays total
Date: 07/20/2023
'''
#Instructions for project
'''
Write a program to accept the yearly salary of five people(one at a time). Using the Accumulation concept, calculate and display the total salary from all five people combined.
'''

#Main Code
print("This program will ask you for 5 different salaries and give you the combined total.\n")

x = 0 
total = 0

while x < 5:
    print('Please enter your salary: ')
    salary = input()
    if salary.isdigit():
        salary = int(salary)
        total += salary
        x += 1
    else:
        print("Please enter a valid number.")
        
print(f"The total of combined salaries is: ${total}")