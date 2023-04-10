
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
    val0 = 0
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
    print(val0)        
    ch = input("Do you want to continue(y/n)? : ")     
         
         
         
         
