'''
Given an array of integers nums which is sorted in ascending order, and an
integer target, write a function to search target in nums.
If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if len(nums) == 0:
            return -1
        
        low, high = 0, len(nums) - 1
        
        while low <= high:
            
            middle = (low + high) // 2
            
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                low = middle + 1
            elif nums[middle] > target:
                high = middle -1
        
        return -1