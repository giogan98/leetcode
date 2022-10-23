'''
Given a string s which consists of lowercase or uppercase letters, return the 
length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome 
here.
'''
class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        # Use a dictionary to keep track of the characters and their occurrences
        dict = {}
        
        # Update the dictionary keys and values
        for char in s:
            if char in dict:
                dict[char] += 1
            else:
                dict[char] = 1
            
        length = 0
        # One time in case of a middle char who can be present only once
        one_time = True
        
        for key, value in dict.items():
            
            length += value // 2 * 2
            dict[key] -= value // 2 * 2
            
            if dict[key] > 0 and one_time:
                dict[key] -= 1
                length += 1
                one_time = False
        
        return length