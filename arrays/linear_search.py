"""
Problem: Linear Search
Find the index of a target element in an array
"""

arr = [10,20,30,40]
target = 30

index = -1

for i in range(len(arr)):
    if arr[i] == target:
        index = i
        break

print(index)
