'''
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a
single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the
number 0 itself.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Use root to store the first node to return
        root = head = ListNode(0)
        carryover = 0
        
        # We exit only when both heads of the lists are Null and there is no carryover left
        while l1 or l2 or carryover:
            
            if l1:
                carryover += l1.val
                l1 = l1.next
            if l2:
                carryover += l2.val
                l2 = l2.next
                
            # Sum the two values of the nodes, if value exceeds 9,
            # report the remainder to the next node 
            value = carryover % 10
            carryover = carryover // 10
            
            # Store the value from 0 to 9 in the next listnode,
            # update the current listnode to the next one
            head.next = ListNode(value)
            head = head.next
                
        
        return root.next