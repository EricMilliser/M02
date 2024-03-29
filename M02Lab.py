'''
M02 M02 Lab - Case Study: if...else and while

A calculator that compares the values of a student and their GPA
to see if they attained the honor roll or Dean's List
'''
'''
Name: M02 Lab - Case Study: if...else and while
Author: Eric Milliser
Date: 3/29/24
Version: 1
Purpose:
A calculator that compares the values of a student and their GPA
to see if they attained the honor roll or Dean's List

Variable list:
lastname (string) = last name of the student
firstname (string) = firstname of the student
gpa (float) = value of the gpa of the student
'''

def endLine():
    print("\n")

def twoEndLine():
    print("\n")

def welcomeMessage(msgToPrint):
    twoEndLine()
    print(msgToPrint)
    twoEndLine()


##DECLARATIONS##
lastname = 'sample string'
firstname = 'sample string'
gpaString = "9.9"
gpa = 9.9




loopCondition = True

welcomeMessage(__doc__)

while (loopCondition == True):
    lastname = input("Enter the student's last name or 'ZZZ'  to quit: ")

    if(lastname == 'ZZZ'):
        loopCondition = False
        break
    else:
        firstname = input("Enter the student's first name: ")
        gpaString = input("Input " + firstname + " " + lastname + "'s GPA on a scale of (0.0-4.0): ")

        gpa = float(gpaString)

        endLine()
        if(gpa >= 3.5):
            print(firstname + " " + lastname + "has made the Dean's List!")
        if (gpa >= 3.25):
            print(firstname + " " + lastname + "has made the Honor Roll!")



twoEndLine()







