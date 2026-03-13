#Sliding_Window

a = [2,3,5,1,3,2]
k = 3

wSum = 0
mSum=float('-inf')

for i in range(0,k):
    wSum = wSum + a[i]

mSum = wSum

for i in range(k,len(a)):
    wSum = wSum - a[i-k] + a[i]
    mSum = max(wSum,mSum)

print("Maximum sum: ",mSum)
