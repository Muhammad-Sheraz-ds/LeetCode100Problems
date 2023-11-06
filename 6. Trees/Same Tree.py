# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p,q):
        if p==q==None:
            return True
        elif p==None or q==None:
            return False
        return self.aux_traversal(p,q)

    def aux_traversal(self,p,q):
        if p==q==None:
            return True
        elif p==None or q==None:
            return False
        elif p.val!=q.val:
            return False
        s1 = self.aux_traversal(p.left,q.left)
        s2 = self.aux_traversal(p.right,q.right)
        if s1==False or s2==False:
            return False
        return True

