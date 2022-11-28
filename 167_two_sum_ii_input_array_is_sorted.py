'''
'''

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # Define binary search of a target number in a sorted list
        # Returns the index of the number if found, else -1
        def binary_search(numbers: List[int], target: int) -> int:
            first, last = 0, len(numbers) - 1

            while first <= last:
                middle = (first + last) // 2
                if numbers[middle] == target:
                    return middle
                elif numbers[middle] < target:
                    first = middle + 1
                else:
                    last = middle - 1
            
            return -1
            
        
        for i in range(len(numbers) - 1):
            
            number_one = numbers[i]
            number_two = target - numbers[i]
            
            index = binary_search(numbers[i+1:], number_two)
            
            if index != -1:
                return [i + 1, (i + index + 2)]

# Alternative solution
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left, right = 0, len(numbers) - 1
        
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1
