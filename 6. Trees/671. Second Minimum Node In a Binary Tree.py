# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root):
        self.ans = []
        min=root.val
        self.traversal(root)
        i=0
        m=-1
        while i < len(self.ans):
            if self.ans[i]>min:
                if m==-1:
                    m = self.ans[i]
                elif self.ans[i]<m:
                    m=self.ans[i]
            i+=1
        return m

    def traversal(self,rt):
        if rt!=None:
            if rt.left!=None:
                self.traversal(rt.left)
            self.ans.append(rt.val)
            if rt.right!=None:
                self.traversal(rt.right)
