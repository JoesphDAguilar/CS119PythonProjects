'''
Programmer Name: Joesph D. Aguilar
Description: Gets user name and 3 test scores, calculates average and displays user's grade
Date: 07/21/2023
'''

#Project Instructions:
'''

Write a program to:

- Ask the student for  3 exam scores.
- Calculate the average score.
- Using a bunch of IF conditions, the computer should determine the grade and display the grade to the user. Use the following Criteria:

* If the Average is 98-100… Assign the grade “A+”
* If the Average is 95-97.99… Assign the grade “A”
* If the Average is 91-94.99… Assign the grade “A-”
* If the Average is 88-90.99… Assign the grade “B+”
* If the Average is 84-87.99… Assign the grade “B”
* If the Average is 80-83.99… Assign the grade “B-”
* If the Average is 75-79.99… Assign the grade “C+”
* If the Average is 70-74.99… Assign the grade “C”
* If the Average is less than 70 and greater than 60 assign a grade “D”
* If the Average is less than or equal to 60 assign a grade "NC"

- Display the student's name 
- Display the grade back to the student.

'''

#Variables
x = 0
gradeTotal = 0
grade = str
userName = str
average = int

#Getting User Input
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

while x < 3:
    print("Enter your grade: ")
    grade = input()
    if grade.isdigit():
        grade = int(grade)
        gradeTotal += grade
        x += 1
        
    else:
        print("please enter a valid number.")
        
#Calculating Average
average = round(gradeTotal / 3)

#Assigning Grade
if average >= 98:
    grade = "A+"
    print(f'{userName} your grade is a {grade}')
elif average <= 97 and average >=95:
     grade = "A"
     print(f'{userName} your grade is a {grade}')
elif average <= 94 and average >= 91:
    grade = "A-"
    print(f'{userName} your grade is a {grade}')
elif average <= 90 and average >= 88:
    grade = "B+"
    print(f'{userName} your grade is a {grade}')
elif average <= 87 and average >= 84:
    grade = "B"
    print(f'{userName} your grade is a {grade}')
elif average <= 83 and average >= 80:
    grade = "B-"
    print(f'{userName} your grade is a {grade}')
elif average <= 79 and average >= 75:
    grade = "C+"
    print(f'{userName} your grade is a {grade}')
elif average <=74 and average >= 70:
    grade = "C"
    print(f'{userName} your grade is a {grade}')
elif average < 70 and average > 60:
    grade = "D"
    print(f'{userName} your grade is a {grade}')
else:
    grade = "NC"
    print(f'{userName} your grade is a {grade}')