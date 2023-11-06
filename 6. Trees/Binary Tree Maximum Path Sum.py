## Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]):
        return self.aux_inorderTraversal(root)

    def aux_inorderTraversal(self, root):
        if root != None:
            ans=root.val
            if root.left != None:
                ans+=root.left.val
                s1 = self.aux_inorderTraversal(root.left)
            if root.right != None:
                ans += root.right.val
                s2 = self.aux_inorderTraversal(root.right)
            return max(ans, s1, s2)
        return -10000000

