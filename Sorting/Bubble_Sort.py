#Bubble Sort
a = [25,75,40,10,20,5,15]
n = len(a)

for i in range(0,n-2):
    for j in range(0,n-2-i):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
print("Sorted array is:")
for i in range(0,n-2):
    print(a[i])
