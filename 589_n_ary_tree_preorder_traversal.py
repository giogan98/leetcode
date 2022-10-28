'''
Given the root of an n-ary tree, return the preorder traversal of its nodes'
values.

Nary-Tree input serialization is represented in their level order traversal.
Each group of children is separated by the None value
'''
# Preoreder traversal:
# 1) Root
# 2) Left sub-tree
# 3) Right sub-tree


# Recursive solution to the problem:
class Solution1:
    def preorder(self, root: 'Node') -> List[int]:
        ans = []

        # Depth first search algorithm:
        def dfs(node):
            
            if not node:
                return
            
            ans.append(node.val)
            
            for child in node.children:
                dfs(child)
        
        dfs(root)
        return ans

# Iterative solution to the problem:
class Solution2:
    def preorder(self, root: 'Node') -> List[int]:
        
        # Edge case with Null tree
        if not root:
            return []
        
        ans = []
        
        queue = [root]
        
        while queue:
            
            # Get the first item
            candidate = queue.pop(0)
            
            ans.append(candidate.val)
            
            for child in reversed(candidate.children):
                queue.insert(0, child)
            
        return ans