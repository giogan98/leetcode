'''
Given the head of a linked list, remove the nth node from the end of the list 
and return its head.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # Dummy node to keep track of head
        dummy = ListNode(0, head)
        
        # Use a two pointers approach, a left one and a right one shifted by n links
        left, right = dummy, head
        
        # Shift the right pointer
        while n > 0 and right:
            right = right.next
            n -= 1
        
        while right:
            right = right.next
            left = left.next
        
        left.next = left.next.next
        
        return dummy.next