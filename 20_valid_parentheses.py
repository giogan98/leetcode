'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']'
determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

'''
class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        dic = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
        
        for c in s:
            if c in dic.keys():
                if len(stack) == 0 or dic[c] != stack.pop():
                    return False
            else:
                stack.append(c)
        
        return len(stack) == 0