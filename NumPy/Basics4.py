import numpy as np

#filtering
ages = np.array([[18,21,17,19,20,16,20,30],
                [15,25,22,24,23,19,21,35]]) 

teenagers = ages[ages<=18]
print(teenagers)
adults = ages[(ages>=18) & (ages <30)]
print(adults)
seniors = ages[ages>=30]
print(seniors)
evens = ages[ages % 2==0]
print(evens)
odds = ages[ages %2 !=0]
print(odds)
adults = np.where(ages >= 18, ages, 0)  #if the age is >= 18 then return the age or else print as 0
print(adults)


#random numbers
rng = np.random.default_rng() #(random number generator) 
rng = np.random.default_rng(seed = 1) #this v will use wen v need to generate the same number
print(rng.integers(1, 7))
print(rng.integers(low = 1, high = 101))
print(rng.integers(low = 1, high = 101, size = (3)))
print(rng.integers(low = 1, high = 101, size = (3, 2)))

print(np.random.uniform()) #random floating point number
print(np.random.uniform(low = -1, high = 1, size = (3,2)))
np.random.seed(seed=1)
print(np.random.uniform(low=-1,high = 1, size =(3,2)))

#this will shuffle the given array
rng1 = np.random.default_rng()
arrayy = np.array([1,2,3,4,5])
rng1.shuffle(arrayy)
print(arrayy)

