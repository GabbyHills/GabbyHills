# -*- coding: utf-8 -*-


'''How to detect two distinct elements

In this problem we will have to receive an array, this array contains numbers and every number repeats at least once, excepto two numbers. You need to create a function that return the two unique numbers.

Example:

return_uniques([1,1,2,2,3,3,4,5,5,6]) -> [4,6]
 
 return_uniques([9,9,2,3,3,3,4,4,10,10,6]) -> [2,6]
 
 return_uniques([10,10,90,90,30,45,45,6,6,6,6,6,6,1]) -> [30,1]
 '''
 # define a function
def return_unique(Lists):
    a = len(Lists)   # assign the maximum element in list to a variable "a"
   
    # a loop for elmination of matched elements 
    for i in range(a):            # create a loop for iteration
     for n in range (i):         # create an inner loop
     # comparisim of element and removal of identical 
             if a!=2 and Lists[n] == Lists[n+1]:  
               Lists.remove(Lists[n])
               Lists.remove(Lists[n])
               print(Lists, a,i)
               a = len(Lists)
             else:
               pass
    print(Lists)
Lists = [10,10,90,90,30,45,45,6,6,6,6,6,6,1]  
return_unique(Lists)
