#Computer assisted multiplication program
#9/1/21
#CSC121 M2Pro- Computer Assisted
#Michel Jurado

# Randomly generate tuplet of two postive one-digit integers
# Use function result to prompt user with a multiplication question
# For correct answer display message "very good!", "Nice work!", and "Keep up the good work!"
# For incorrect answer display "No, Please try again","Wrong. Please try once more.", and "No.Keep trying." and make student keep trying until correct

#Level 3 Exercise 4.16 Page 154

#create a menu to choose between multiplying 1 or 2 digit numbers.
# if 1 or 2 is chosen enter that choices function
#output the multiplication question
#collect inputs and place into variables
#test if correct
#if correct display 3 random correct outputs
#if incorrect display 3 random incorrect outputs and start loop until correct

import  math
import random



def randomint1digit():
    """Output two random one-digit integers"""
    #declaring local variables
    integer1= random.randrange(0,10)
    integer2= random.randrange(0,10)

    CorrectReplies= ["Very good!", "Nice work!", "Keep up the good work!"]
  
    InCorrectReplies= ["No.Please try again.", "Wrong,Please try once more.", "No, keep trying."]
  
    #finish declarations--------------------------------------

    #start gathering input

    print(f'How much is {integer1} times {integer2}')
    print('\t')
    answer= int(input("Enter solution: "))
    
    if answer == integer1 * integer2 :
        print(random.choice(CorrectReplies)) #will randomly output correct replies

    else:
        print(random.choice(InCorrectReplies))
        #get stuck in loop until correct

        while answer != integer1 * integer2:
            answer= int(input("Enter solution: "))

            if answer != integer1 * integer2:
                print(random.choice(InCorrectReplies)) #will randomly output in1correct replies

            else: 
                print(random.choice(CorrectReplies)) # end of function and will randomly output correct replies

#----------------

def randomint2digit():
    """Output two random one-digit integers"""
    #declaring local variables
    integer1= random.randrange(0,100)
    integer2= random.randrange(0,100)

    CorrectReplies= ["Very good!", "Nice work!", "Keep up the good work!"]
  
    InCorrectReplies= ["No.Please try again.", "Wrong,Please try once more.", "No, keep trying."]
  
    #finish declarations--------------------------------------

    #start gathering input

    print(f'How much is {integer1} times {integer2}')
    print('\t')
    answer= int(input("Enter solution: "))
    
    if answer == integer1 * integer2 :
        print(random.choice(CorrectReplies)) #will randomly output correct replies

    else:
        print(random.choice(InCorrectReplies))
        #get stuck in loop until correct

        while answer != integer1 * integer2:
            answer= int(input("Enter solution: "))

            if answer != integer1 * integer2:
                print(random.choice(InCorrectReplies)) #will randomly output in1correct replies

            else: 
                print(random.choice(CorrectReplies)) # end of function and will randomly output correct replies


#menu to choose difficulty

print("Choose difficulty 1 or 2" '\t' "1= one digit numbers 2= two digit numbers")
answer= int(input("Enter 1 or 2:"))

if answer == 1:
    randomint1digit()
else:
    randomint2digit()
