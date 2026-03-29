import numpy as ap

array1 = ap.array([[1,2,3,4],
                   [5,6,7,8],
                   [9,10,11,12],
                   [13,14,15,16]])
array2 = ap.array([[1], [2], [3],[4]])

print(array1.shape)
print(array2.shape)
print(array1*array2)


array = ap.array([[1,2,3,4,5],
                  [6,7,8,9,10]])
print(ap.sum(array)) #sum of all the elemnts
print(ap.mean(array)) #mean 
print(ap.std(array)) #Standard Deviation
print(ap.var(array)) #Variance
print(ap.min(array)) #minimum
print(ap.max(array)) #maximum
print(ap.argmin(array)) #position of min value
print(ap.argmax(array)) #position of max value
print(ap.median(array)) #median
print(ap.sum(array,axis = 0)) #adds the columns of array
print(ap.sum(array,axis = 1)) #adds the rows of array


