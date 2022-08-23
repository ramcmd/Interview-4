# TC: O(n)
# SC: recursive stack O(height of the tree)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # Base condition\
        self.flag = True
        
        self.traversal(root)
        
        return self.flag
    
    def traversal(self, root):
        
        # base condition
        if root == None:
            return 0
        
        # goes to the leaf node
        leftht = self.traversal(root.left)
        # goes to the leaf node
        rightht = self.traversal(root.right)
        
        if abs(leftht - rightht) > 1:
            self.flag = False
        
        return max(leftht, rightht) + 1
        
        
        
            
            