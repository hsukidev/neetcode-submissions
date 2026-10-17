import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        droppedPunctuation = s.maketrans("","", string.punctuation)
        sanitizedString = s.translate(droppedPunctuation).replace(" ", "").lower()

        i = 0
        j = len(sanitizedString) - 1

        while i <= j:
            if sanitizedString[i] != sanitizedString[j]:
                return False
            i = i + 1
            j = j - 1
        return True

## Problem
# Given a string s, return true if it is a palindrome, otherwise return false.
# A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

## Pattern
# two-pointer

## Approach
# Sanitize string first for spaces and special characters
# Pointers at start and end of sanitized string
# Increment first pointer, decrement second pointer

## Complexity
# Time = O(n), Space = O(n)

## Insight
# Instead of allocating a new string with translate()/replace()/lower(), use custom alphanumeral filtering function to traverse original string in place