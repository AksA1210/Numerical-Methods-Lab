# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 22:48:59 2023

@author: user
"""

# Defining Function
def f(x):
    return x**3-4*x-9

    '''degree = int(input("Enter the degree : "))
    for i in range(degree,0,-1):
        a = int(input("Enter the coefficient of : ","x^",degree))
     '''   
    
# Implementing False Position Method
def falsePosition(x0,x1,e):
    step = 1
    print('\n\n*** FALSE POSITION METHOD IMPLEMENTATION ***')
    condition = True
    while condition:
        x2 = x0 - (x1-x0) * f(x0)/( f(x1) - f(x0) )
        print('Iteration-%d, x2 = %0.6f and f(x2) = %0.6f' % (step, x2, f(x2)))

        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2

        step = step + 1
        condition = abs(f(x2)) > e

    print('\nRequired root is: %0.8f' % x2)


# Input Section
x0 = input('First Guess: ')
x1 = input('Second Guess: ')
e = input('Tolerable Error: ')

# Converting input to float
x0 = float(x0)
x1 = float(x1)
e = float(e)

#Note: You can combine above two section like this
# x0 = float(input('First Guess: '))
# x1 = float(input('Second Guess: '))
# e = float(input('Tolerable Error: '))


# Checking Correctness of initial guess values and false positioning
if f(x0) * f(x1) > 0.0:
    print('Given guess values do not bracket the root.')
    print('Try Again with different guess values.')
else:
    falsePosition(x0,x1,e)




''''Output
First Guess: 2

Second Guess: 3

Tolerable Error: 0.005


*** FALSE POSITION METHOD IMPLEMENTATION ***
Iteration-1, x2 = 2.600000 and f(x2) = -1.824000
Iteration-2, x2 = 2.693252 and f(x2) = -0.237227
Iteration-3, x2 = 2.704918 and f(x2) = -0.028912
Iteration-4, x2 = 2.706333 and f(x2) = -0.003495

Required root is: 2.70633349

''''
