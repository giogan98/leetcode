'''
Given a linked list, swap every two adjacent nodes and return its head.
You must solve the problem without modifying the values in the list's nodes
(i.e., only nodes themselves may be changed.)
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Create a root and head to store the new swapped linked list
        root = temp = ListNode(0)
        
        # Swap the linked lists two nodes at the time
        while head and head.next:
            previous = ListNode(head.val)
            current = ListNode(head.next.val)
            
            temp.next = current
            temp.next.next = previous
            temp = temp.next.next
            head = head.next.next
        
        # In case of a odd sized linked list
        if head:
            temp.next = head
            
        return root.next