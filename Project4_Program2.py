'''
Programmer Name: Joesph D. Aguilar
Description: Determines contestant's average score and displays it using functions
Date: 08/14/2023
'''

#Project Instructions

'''
A particular talent competition has 5 judges, each of whom awards a score between 0 and
10 to each performer. Fractional scores, such as 8.3, are allowed. A performer's final score
is determined by dropping the highest and lowest score received, then averaging the 3
remaining scores. Write a program that uses these rules to calculate and display a
contestant's score. It should include the following functions:

• getJudgeData() should ask the user for a judge's score, store it in a 
parameter variable, and validate it. This function should be called by main program once for each
of the 5 judges.

• calcScore(score1, score2, score3, score4, score5) should calculate and return the average of the 3 scores that
remain after dropping the highest and lowest scores the performer received. This
function should be called just once by main and should be passed the 5 scores.
Two additional functions, described below, should be called by calcScore, which uses the
returned information to determine which of the scores to drop.

• findLowest(score1, score2, score3, score4, score5) should find and return the lowest of the 5 scores passed to it. 
Note: You are not allowed to use min() function

• findHighest(score1, score2, score3, score4, score5) should find and return the highest of the 5 scores passed to it. 
Note: You are not allowed to use max() function

'''

#Start of Code

'''
Functions
'''

#Gets judges score and validates if score is between 0 and 10
def getJudgeData():
    while True:
        try:
            score = float(input("Enter score: "))
            
            if score >= 0 and score <= 10:
                return score
            else:
                print("Error: Score must be between 0 through 10!")
                continue
        except ValueError:
            print('Error: Please enter a valid score!')
            continue


#Takes 5 scores and returns lowest score
def findLowest(score1, score2, score3, score4, score5):
    scoreList = [score1, score2, score3, score4, score5]
    lowestScore = sorted(scoreList)
    return lowestScore[0]


#Takes 5 scores and returns the hightest
def findHighest(score1, score2, score3, score4, score5):
    scoreList = [score1, score2, score3, score4, score5]
    highestScore = sorted(scoreList, reverse = True)
    return highestScore[0]

#Finds the lowest and highest score and returns the average of the 3 scores that remain
def calcScore(score1, score2, score3, score4, score5):
    scoreList = [score1,score2, score3, score4, score5]
    
    lowest = findLowest(score1,score2, score3, score4, score5)
    highest = findHighest(score1,score2, score3, score4, score5)
    scoreList.remove(lowest)
    scoreList.remove(highest)
    
    return sum(scoreList) / len(scoreList)
  

'''
Variables
'''

judge1Score = None
judge2Score = None
judge3Score = None
judge4Score = None
judge5Score = None
finalScore = None


'''
Main code
'''

#First Judge score
print('Judge 1 enter your score.')
judge1Score = getJudgeData()

#Second Judge score
print('Judge 2 enter your score.')
judge2Score = getJudgeData()

#Third Judge score
print('Judge 3 enter your score.')
judge3Score = getJudgeData()

#Fourth Judge score
print('Judge 4 enter your score.')
judge4Score = getJudgeData()

#Fifth Judge score
print('Judge 5 enter your score.')
judge5Score = getJudgeData()

finalScore = calcScore(judge1Score, judge2Score, judge3Score, judge4Score, judge5Score)
finalScore = round(finalScore, 2)
print(f"\nContestant's Final Score: {format(finalScore, '.2f')}")

#End of code