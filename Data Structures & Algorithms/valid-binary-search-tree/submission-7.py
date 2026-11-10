# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True
        if not root.right:
            return True
        if not root.left:
            return True
        right = root.right
        left = root.left

        if root.val >= right.val or root.val <= left.val:
            return False
        else:
            return self.isValidBST(root.left) and self.isValidBST(root.left)