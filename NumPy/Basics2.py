# basics
import numpy as np

#SLICING

array = np.array([[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12],
                  [13,14,15,16]])
print(array[1:,:]) #start:stop:step  
print(array[1:3,1:3])  #row,column 


#ARITHMETIC

array1 = np.array([1.23,2,4.5]) 
print(array1+1)
print(np.round(array1))


array2 = np.array([1,2,3])
array3 = np.array([4,5,6])
print(array2+array3)
