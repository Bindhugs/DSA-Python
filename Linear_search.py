arr = []
n = int(input("Enter number of elements: "))

for i in range(n):
    val = int(input("Enter element: "))
    arr.append(val)

key = int(input("Enter element to search: "))
found = False
for i in range(n):
    if arr[i] == key:
        print("Element found at position", i + 1)
        found = True
        break

if not found:
    print("Element not found")