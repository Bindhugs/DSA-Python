#Fibonacci Series

n = int(input("Enter the number of elements: "))

def Fibonacci(n):
    if n<=1:
        return n
    else: 
        return Fibonacci(n-1)+Fibonacci(n-2)

print("Fibonacci series: ")

for i in range(n):
    print(Fibonacci(i))