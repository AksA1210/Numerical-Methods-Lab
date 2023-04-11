# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 14:28:54 2023

@author: cusat
"""
def check_range(A,B,nterms):
    x0 = 0
    x1 = 1
    #finding f(0)
    i=0
    j=0
    while (i<nterms):
        if (B[j] == 0):
            x0 = x0+A[i]
            print(x0)
        else:
            x0 = x0+(A[i]*(0**B[j]))
            print(x0)
        i += 1
        j += 1
    #finding f(1)
    i=0
    j=0
    while (i<nterms):
        if (B[j] == 0):
            x1 = x1+A[i]
            print(x1)
        else:
            x1 = x1+(A[i]*(0**B[j]))
            print(x1)
        i += 1
        j += 1
    print(x1)
    if ((x0>0 and x1<0) or (x0<0 and x1>0)):
        x2 = (x0+x1)/2
    else:
        x1 = -1
        
    
ch = 'y'
while ch == 'y':
    print("----------------BISECTION METHOD---------------")
    degree = int(input("Enter the degree of the equation : "))
    A = []
    i = degree
    while(i>=0):
        print("Enter the coefficient of x^",i," : ")
        A.append(int(input()))
        i = i - 1
    print("EQUATION : ")   
    i = degree + 1
    while(i!=0):
        for j in A : 
            if(j > 0):
                print(j,"x ^",i - 1,"+")
            elif (j < 0) :
                print(j,"x ^",i - 1," ")
            else:
                print()
                print(" ")   
            i = i - 1
    print()        
    B = []
    while(degree>=0):
        B.append(degree)
        degree = degree - 1
    for i in B:
        print(i) 
    print()    
    nterms = degree+1 
    #finding f(0) and f(1)
    '''val0 = 0
    i=0
    j=0
    while (i<nterms):
        if (B[j] == 0):
            val0 = val0+A[i]
            print(val0)
        else:
            val0 = val0+(A[i]*(0**B[j]))
            print(val0)
        i += 1
        j += 1
    print(val0)  '''
    check = check_range()        
    ch = input("Do you want to continue(y/n)? : ")     
         







       
         
         
