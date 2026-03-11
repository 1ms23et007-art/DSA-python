"""
Source: HackerRank
Problem: Reverse an Array
Topic: Arrays
Difficulty: Easy

Problem Description:
Given an array of integers, reverse the array and print the reversed array.

Example:
Input: 1 2 3 4
Output: 4 3 2 1

Pseudocode:
1. Start with two pointers
2. Left pointer at index 0
3. Right pointer at index n-1
4. Swap elements at left and right
5. Move left forward and right backward
6. Continue until left >= right

Time Complexity: O(n)
Space Complexity: O(1)
"""


def reverseArray(A):
    left = 0
    right = len(A) - 1

    while left < right:
        temp = A[left]
        A[left] = A[right]
        A[right] = temp

        left += 1
        right -= 1

    return A


# Main Program
if __name__ == "__main__":
    N = int(input().strip())
    A = list(map(int, input().split()))

    reversed_array = reverseArray(A)

    for num in reversed_array:
        print(num, end=" ")
