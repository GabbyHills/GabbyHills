# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 13:14:27 2022

@author: LENOVO
"""

"""Code Challenge #2

How can I find the vowels?

Which function help me to takes a string and returns the number(counts)of vowels contained within it.

Examples:
count_vowels("Elephant")-> 3
 count_vowels("car")->1
 count_vowels("computer")->3
 
 """
 # Define a function to check the vowels
def isVowel(vowels):
     return vowels.upper() in ['A','E','I','O','U']
 
 
 # Define a function to return the vowels in a string
def count_Vowel(str):
     count = 0  # initiating a counting variable

     for i in range(len(str)):   # initiating a loop for checking vowels in string
       if isVowel(str[i]):     # using "isVowel" function to check for vowel
           count += 1         # axxumulating the count 
     return count            # Return the count
 
    
Statement=("what are yoiu doing today my bill and day")
count_Vowel(Statement)
print(count_Vowel(Statement))
