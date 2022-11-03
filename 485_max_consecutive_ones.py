'''
Given a binary array nums, return the maximum number of consecutive 1's in the
array.
'''
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        consecutives, max_consecutives = 0, 0
        
        for num in nums:
            
            if num == 1:
                consecutives += 1
            else:
                max_consecutives = max(consecutives, max_consecutives)
                consecutives = 0
        
        # In case the last element is a 1 and not a 0
        max_consecutives = max(consecutives, max_consecutives)
        
        return max_consecutives