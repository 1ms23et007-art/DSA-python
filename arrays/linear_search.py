""" 
Source: Self Learning
Difficulty: Easy
Topic: Arrays
Problem: Linear Search

Approach:
Traverse the array and compare each element with the target.

Time Complexity: O(n)
Space Complexity: O(1)
"""

arr = [10,20,30,40]
target = 30

index = -1

for i in range(len(arr)):
    if arr[i] == target:
        index = i
        break

print(index)
