class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        max_length = max(len(word1), len(word2))
        new_word = ''
        for i in range(0, max_length):
            if i < len(word1):
                new_word += word1[i]
            if i < len(word2):
                new_word += word2[i]

        return new_word

## Problem
# You are given two strings, word1 and word2. Construct a new string by merging them in alternating order, starting with word1 — take one character from word1, then one from word2, and repeat this process. If one string is longer than the other, append the remaining characters from the longer string to the end of the merged result. Return the final merged string.

## Pattern
# two pointer

## Approach
# check each word until max_len of that word

## Complexity
# Time: O(n + m)
# Space: O(n + m) 

## Insight
# this problem can be solved with one pointer