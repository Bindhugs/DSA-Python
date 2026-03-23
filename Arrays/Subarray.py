#Sum of subarray = The total obtained by adding all elements of a portion of array

arr = [1,2,3]
for i in range(len(arr)):
    sum = 0
    for j in range(i,len(arr)):
        sum = sum + arr[j]
        print("Subarray sum: ",sum)
