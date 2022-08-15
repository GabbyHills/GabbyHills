# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 12:56:57 2022

@author: LENOVO
"""

"""
Code Challenge Launch #2
***Code Challenge #2

Prefixes vs Suffixes

Create two functions
isPrefix(word,prefix)
isSuffix(word,suffix)

IsPrefix should return true if we begins with the prefix
isSuffix should return true if ends with the suffix

Otherwise return false.

Examples

isPrefix("automatic","auto") -> true
isSuffix("aracnophobia","phopia") -> true
isPrefix("airplane","plane") -> false
isSuffix("computer","vowel") -> false
"""
# define a prefix check function
def isPrefix(str, prefix):                 # assign variables and its prefix to the function
    status = str.startswith(prefix)
    return print(status)

'''#   below code can achieve it for biginners
def isPrefix(str, prefix):  
    prefixLength = len(prefix)                 # get the lenght of the prefix and save in variable "prefixLength"     
    beginStr = str[0:prefixLength]         # spilt the strings element and save in variable "beginStr" 
    if beginStr == prefix:                 # compare the two strings
        return print('true')               # if the varible comparison is true printout "true"
    else:
        return print('false')              # if the varible comparison is false printout "false"
'''

# below code will do the same in two line code
#define a suffix check function
def isSuffix(str, suffix):                 # assign variables and its suffix to the function
        status = str.endswith(suffix)
        return print(status)
''' 
def isSuffix(str, suffix):   
suffixLength = len(suffix)                 # get the lenght of the suffix and save in variable "suffixLength"      
    strLength = len(str)                   # get the lenght of the charater and save in variable "strLength"     
    checkStart = strLength-suffixLength    # get the split position and save in variable "checkStart
    strSuffix = str[checkStart:]           # spilt the strings element and save in variable "strSuffix
    if strSuffix == suffix:                # # if the varible comparison is true printout "true"
        return print('true')
    else:
        return print('false')              # if the varible comparison is false printout "false"
'''
str,prefix = "aracnophobia","a"
isPrefix(str, prefix)
str, suffix = "computer","vowel"
isSuffix(str, suffix)