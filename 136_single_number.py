'''
Given a non-empty array of integers nums, every element appears twice except
for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only
constant extra space.
'''

# Method 1
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        # Keep track of the numbers in a dict, delete when a pair is found
        nums_dict = {}
        
        for num in nums:
            if num in nums_dict:
                del nums_dict[num]
            else:
                nums_dict[num] = 1
        
        # In the end only the single number remains
        return list(nums_dict.keys())[0]

# Method 2:
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        # Use the XOR operator to find the only single number
        for i in range(1, len(nums)):
            nums[0] ^= nums[i]
            
        return nums[0]