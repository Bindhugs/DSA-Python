#Find the largest element in an array

a = list(map(int,input("Enter the elements of the array: ").split()))
#takes user input and converts it into a list of integers

largest = a[0]
for i in range(1,len(a)):
    if a[i] > largest: 
        #checks if the current element is largest than the larger element
        largest = a[i] 
print("The largest element in the array is: ",largest) 
#prints the largest element in the array
