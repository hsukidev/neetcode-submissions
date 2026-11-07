class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            # find offset from l to get to midpoint, then add back in l to get the actual index
            m = l + ((r - l) // 2)

            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1

## Problem
# You are given an array of distinct integers nums, sorted in ascending order, and an integer target.
# Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.
# Your solution must run in O(logn) time.

## Pattern
# iterative binary search

## Approach
# 2 pointer, moving l and r and calculating midpoint

## Complexity
# Time: O(logn)
# Space: 1

## Insight
# calculate m offset from l to get to r, add back in l to get actual m index 
# adjust l and pointer accordingly