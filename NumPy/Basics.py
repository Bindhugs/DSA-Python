# Basics
import numpy as np
a = np.array('A') #0d
b= np.array(['a','b']) #1d
c = np.array([['a','b'],['k','l']]) #2d
print(a)
print(a.ndim) #Tells the dimension
print(b.shape) #Tells the size of matrix
print(b.itemsize) #size of the item

array = np.array([[['A','B','C'],['D','E','F'],['G','H','I']],
                   [['J','K','L'],['M','N','O'],['P','Q','R']],
                   [['S','T','U'],['V','W','X'],['Y','Z',' ']]])  #3d
print(array)

#Accessing letter
print(array[0,2,1]) #depth/layer,row,column

#Forming words
word = array[1,1,1]+array[0,0,0]+array[1,1,0]+array[0,0,0]+array[2,0,0]+array[2,0,1]+array[0,1,1]
print(word)
