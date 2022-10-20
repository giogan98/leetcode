'''
Given two strings s and t, return true if s is a subsequence of t, or false 
otherwise.

A subsequence of a string is a new string that is formed from the original 
string by deleting some (can be none) of the characters without disturbing the
relative positions of the remaining characters. (i.e., "ace" is a subsequence of 
"abcde" while "aec" is not).
'''

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        # Edge cases
        if s == t:
            return True
        if len(s) == 0:
            return True
        if len(s) > len(t):
            return False

        # Check if there are letters in order to remake the string s in t
        index = 0
        for char in s:
            # Find character in a substring of t
            found = t[index:].find(char)
            if found == -1:
                return False
            else:
                # Go to the next character
                index += found + 1
        return True


s1, t1 = "abc", "ahbgdc"
s2, t2 = "axc", "ahbgdcccc"
s3, t3 = "aaaaaa", "bbaaaa"
solution = Solution()
# True:
print(solution.isSubsequence(s1, t1))
# False:
print(solution.isSubsequence(s2, t2))
# False:
print(solution.isSubsequence(s3, t3))