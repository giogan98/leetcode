# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # We need two ListNodes to keep track of the first head
        # The first head will be initialized to 0, None
        ans = dummy = ListNode()
        
        # Confront the values of each list, link the smallest as the next value in the dummy NodeList
        while list1 and list2:
            if list1.val <= list2.val:
                dummy.next = list1
                list1 = list1.next
                dummy = dummy.next
            else:
                dummy.next = list2
                list2 = list2.next
                dummy = dummy.next
        
        # When one or both lists are Null, simply append the list as the next link to the dummy NodeList
        if not list1:
            dummy.next = list2
        elif not list2:
            dummy.next = list1
        
        return ans.next