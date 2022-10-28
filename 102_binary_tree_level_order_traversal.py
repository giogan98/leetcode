'''
Given the root of a binary tree, return the level order traversal of its nodes'
values. (i.e., from left to right, level by level).
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # Edge case of Null tree
        if not root:
            return []
        
        # We can find the solution using a queue
        ans = []
        q = [root]
        
        while q:
            # Append the list of the values of the nodes in the q
            level = []
            for node in q:
                level.append(node.val)
            ans.append(level)
            # Update the q with the nodes chilren
            sublevel = []
            for node in q:
                if node.left:
                    sublevel.append(node.left)
                if node.right:
                    sublevel.append(node.right)
            q = sublevel
        
        return ans