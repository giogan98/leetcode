'''
Given an integer array nums, return true if any value appears at least twice
in the array, and return false if every element is distinct.
'''

# Method 1
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        nums_dict = {}
        
        for num in nums:
            if num in nums_dict:
                return True
            nums_dict[num] = 1
        
        return False

# Method 2
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)