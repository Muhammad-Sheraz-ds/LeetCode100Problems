# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root):
        if root == None:
            return True
        return self.aux_traversal(root.left, root.right)

    def aux_traversal(self, p, q):
        if p == q == None:
            return True
        elif p == None or q == None:
            return False
        elif p.val != q.val:
            return False
        s1 = self.aux_traversal(p.left, q.right)
        s2 = self.aux_traversal(p.right, q.left)
        if s1 == False or s2 == False:
            return False
        return True