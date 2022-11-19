'''
Given the root of a binary tree, return the inorder traversal of its nodes'
values.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        #INORDER TRAVERSAL:
        #1) traverse the left subtree
        #2) visit the root
        #3) traverse the right subtree
        
        ans = []
        
        def recursive_traversal(node: Optional[TreeNode]) -> int:
            
            if node:
                recursive_traversal(node.left)
                
                ans.append(node.val)
                
                recursive_traversal(node.right)
        
        recursive_traversal(root)
        
        return ans
                
                