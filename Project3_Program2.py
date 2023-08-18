'''
Programmer Name: Joesph D. Aguilar
Description: This program helps analyze data for runners
Date: 08/09/2023
'''

#Project Instructions

'''

Please make sure to have all the inputs be entered by the user not hardcoded. 

Mike, Tina, Jason, Vicky, and Tammy are preparing for an upcoming marathon. 
Each day of the week, they run a certain number of miles and write them into a notebook. 
At the end of the week, they would like to know the number of miles run each day, the total miles for the week, 
and average miles run each day, Write a program to help them analyze their data. Your program must contain parallel 
lists: a list to store the the names of the runners and a two-dimensional list of five rows and seven columns to store 
the number of miles run by each runner each day.  

Sample Output:

Name  Day 1   Day 2    Day 3    Day 4   Day 5   Day 6   Day 7   Average

=============================================
Mike   10.00   15.00    20.00   25.00    18.00    20.00    26.00    19.14
Tina     15.00  18.00    29.00   16.00     26.00    20.00    23.00    21.00
Jason   20.00  26.00  18.00     29.00   10.00    12.00     20.00    19.29
Vicky    17.00   20.00 15.00    26.00    18.00    25.00    12.00    19.00
Tammy 16.00   8.00    28.00    20.00    11.00    25.00    21.00   18.43

'''

#importing mean() to use calculate the average runtime later in program
from statistics import mean

#Defining main variables
runName = ['runner1', 'runner2', 'runner3', 'runner4', 'runner5']
weekTime = ['time1', 'time2', 'time3', 'time4', 'time5', 'time6', 'time7']
daysAve = [['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5', 'Day 6', 'Day 7'],[]]
runLen = len(runName)
weekTime = len(weekTime)
days = len(daysAve[0])
userName = None
userTime = None
average = None
averageTotal = None

#Runners times
runnerOne = []
runnerTwo = []
runnerThree = []
runnerFour = []
runnerFive = []

#Getting runner's names
for x in range(runLen):
    while True:
        print('Please enter your name.')
        userName = input('Name: ')
        
        if not userName.isdigit():
            runName[x] = userName.capitalize()
            print('Thank you. Next')
            break
        else:
            print('Error: Please enter letters only!')
            
#Getting runner one's time
for x in range(weekTime):
    while True:
        print('\nRunner One please enter your times. Ex(00.00)')
        userTime = input(f'Day {x + 1}: ')
        userTime = float(userTime)
        userTime = round(userTime, 2)
        
        if (isinstance(userTime, float)):
            runnerOne.append(userTime)
            average = mean(runnerOne)
            averageTotal = round(average, 2)
            break
        else:
            print('Error: Please enter numerical digits only!')
    
daysAve[1].append(averageTotal) 

#Getting runner two's time
for x in range(weekTime):
    while True:
        print('\nRunner Two please enter your times. Ex(00.00)')
        userTime = input(f'Day {x + 1}: ')
        userTime = float(userTime)
        userTime = round(userTime, 2)
        
        if (isinstance(userTime, float)):
            runnerTwo.append(userTime)
            average = mean(runnerTwo)
            averageTotal = round(average, 2)
            break
        else:
            print('Error: Please enter numerical digits only!')
    
daysAve[1].append(averageTotal) 

#Getting runner three's time
for x in range(weekTime):
    while True:
        print('\nRunner three please enter your times. Ex(00.00)')
        userTime = input(f'Day {x + 1}: ')
        userTime = float(userTime)
        userTime = round(userTime, 2)
        
        if (isinstance(userTime, float)):
            runnerThree.append(userTime)
            average = mean(runnerThree)
            averageTotal = round(average, 2)
            break
        else:
            print('Error: Please enter numerical digits only!')
    
daysAve[1].append(averageTotal) 

#Getting runner fours's time
for x in range(weekTime):
    while True:
        print('\nRunner four please enter your times. Ex(00.00)')
        userTime = input(f'Day {x + 1}: ')
        userTime = float(userTime)
        userTime = round(userTime, 2)
        
        if (isinstance(userTime, float)):
            runnerFour.append(userTime)
            average = mean(runnerFour)
            averageTotal = round(average, 2)
            break
        else:
            print('Error: Please enter numerical digits only!')
    
daysAve[1].append(averageTotal)

#Getting runner five's time
for x in range(weekTime):
    while True:
        print('\nRunner five please enter your times. Ex(00.00)')
        userTime = input(f'Day {x + 1}: ')
        userTime = float(userTime)
        userTime = round(userTime, 2)
        
        if (isinstance(userTime, float)):
            runnerFive.append(userTime)
            average = mean(runnerFive)
            averageTotal = round(average, 2)
            break
        else:
            print('Error: Please enter numerical digits only!')
    
daysAve[1].append(averageTotal)

#Displaying everything
print('\n Name ', *daysAve[0], 'Average')
print(" ========================================================")
print(f' {runName[0]} ', *runnerOne, f' {daysAve[1][0]}')
print(f' {runName[1]} ', *runnerTwo,  f' {daysAve[1][1]}')
print(f'{runName[2]} ', *runnerThree, f' {daysAve[1][2]}')
print(f'{runName[3]} ', *runnerFour, f' {daysAve[1][3]}')
print(f'{runName[4]} ', *runnerFive, f' {daysAve[1][4]}')