
ch = 'y'
while ch == 'y':
    print("----------------BISECTION METHOD---------------")
    degree = int(input("Enter the degree of the equation : "))
    A={}
    i = degree
    key = i
    value = A[key]
    while(i>=0):
        print("Enter the coefficient of x^",i," : ")
        A.append(int(input()))
        i = i - 1
    print("EQUATION : ")   
    i = degree + 1
    key = i
    while(i!=0):
        for val in A : 
            if(A[key] > 0):
                print(value,"x ^",i - 1,"+")
            elif (A[key] < 0) :
                print(A[key],"x ^",i - 1," ")
            else:
                print()
                print(" ")   
            i = i - 1
    #n_terms = degree+1 
    #finding f(0) and f(1)
    
    ch = input("Do you want to continue(y/n) ? : ")     
