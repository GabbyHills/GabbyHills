# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 10:24:20 2022

@author: Gabby
"""
"""
Code Challenge Launch #2
***Code Challenge #1

Return the Middle Character(s) of a String

You need to create a function to takes a string and returns the middle characters(s). 
If the words length is odd return the middle, buy if the words length is even 
return the middle 2 characters.


Examples

getMiddle("coin") -> "oi"
getMiddle("books")-> "o"
getMiddle("computer")-> "pu"
getMiddle("O") -> O

Notes:
All test cases must contain a single word

"""
# define a function "getMiddle"
def getMiddle(str): #set the accept the input value
    
    letter = [int for (str) in (str) ] # Covert string to List
    letterLength = len(letter)
    
    middlePos = letterLength//2 # set the middle position of type real no
    middlePos1 = letterLength/2 # set the middle position of type float
    displayDecision = middlePos - middlePos1 # set a decision variable
    
    # A loop for decision 
    if displayDecision == 0:   # check the the type 
       
    # return the value of the two middle character
        return print(str[middlePos],str[middlePos-1])
    else:
        # return value for one middle character
        return print(str[middlePos])
letter = 'booking'
getMiddle(letter)       