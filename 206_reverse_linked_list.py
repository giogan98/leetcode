'''
Given the head of a singly linked list, reverse the list, and return the 
reversed list.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # We will use a two pointer approach to solve the problem
        prev = None
        
        while head:
            current = head
            head = head.next
            current.next = prev
            prev = current
            
        return prev        