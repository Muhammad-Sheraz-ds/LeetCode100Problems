# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root, k):
        self.ans = []
        self.traversal(root)
        return self.ans[len(self.ans)-k]

    def traversal(self,rt):
        if rt!=None:
            if rt.left!=None:
                self.traversal(rt.left)
            self.ans.append(rt.val)
            if rt.right!=None:
                self.traversal(rt.right)
