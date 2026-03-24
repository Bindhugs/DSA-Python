#FINDING FACTORIAL USING RECURSION

n = int(input("Enter the number to find factorial: \n"))
#Taking input from user

def factorial(n):
    if n==0 or n==1: 
        return 1
    else: 
        return n * factorial(n-1)

#recursion 

result = factorial(n)    
print("Factorial for given number is: ",result)

#printing result
