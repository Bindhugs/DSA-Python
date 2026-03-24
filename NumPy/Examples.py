import numpy as np

#EXAMPLE1

radii = np.array([10])
area = np.pi * radii ** 2  #area = pi*r**2
perimeter = np.pi * radii  #perimeter = pi*r
print("Area of circle is: ",area)
print("Area rounded of to - ",(np.round(area)))
print("Perimeter of circle is: ",perimeter) 
print("Perimeter rounded of to - ",(np.round(perimeter)))


# EXAMPLE2

marks = np.array([12,34,54,67,87,90,100,67])
print(marks)
print(marks < 50)
marks[marks < 50] = 0
print(marks)