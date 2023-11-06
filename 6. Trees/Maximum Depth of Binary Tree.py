# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root)
        if root == None:
            return 0
        return self.aux_inorderTraversal(root, 1)

    def aux_inorderTraversal(self, root, sum):
        if root != None:
            s1, s2 = sum, sum
            if root.left != None:
                s1 = self.aux_inorderTraversal(root.left, sum + 1)
            if root.right != None:
                s2 = self.aux_inorderTraversal(root.right, sum + 1)
            return max(s1, s2)
