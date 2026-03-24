#Bubble Sort
a = [75, 95, 62, 15, 54, 32]
n = len(a)

for i in range(n):
    for j in range(0,n-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
print("Sorted array is:")
for i in range(n):
    print(a[i])
