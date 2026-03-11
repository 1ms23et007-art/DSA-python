"""
Source: Self Practice
Problem: Find Maximum Element
Topic: Arrays
Difficulty: Easy

Problem Description:
Given an array of integers, find and print the maximum element in the array.

Example:
Input: [3, 7, 2, 9, 1]
Output: 9

Pseudocode:
1. Assume the first element is the maximum
2. Traverse the array from the second element
3. If current element > max_element
4. Update max_element
5. After traversal, return max_element

Time Complexity: O(n)
Space Complexity: O(1)
"""
def findMax(arr):
    max_element = arr[0]

    for i in range(1, len(arr)):
        if arr[i] > max_element:
            max_element = arr[i]

    return max_element

if __name__ == "__main__":
    n = int(input("Enter number of elements: "))
    arr = list(map(int, input("Enter elements: ").split()))

    result = findMax(arr)

    print("Maximum element:", result)
