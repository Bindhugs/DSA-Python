# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]

array = list(map(int, input("Enter the array: ").split()))
target = int(input("Enter the target element: "))

found = False

for i in range(len(array)):
    for j in range(i+1, len(array)):
        if array[i] + array[j] == target:
            print([i], "+",[j], "=", target)
            found = True

if not found:
    print("No pair found")