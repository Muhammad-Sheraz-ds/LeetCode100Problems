# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def min_(self,root):
        if root!=None:
            if root.val<self.less:
                self.less=root.val
            self.min_(root.left)

    def max_(self,root):
        if root!=None:
            if root.val>self.gr:
                self.gr=root.val
            self.max_(root.right)
    def closestNodes(self, root, queries):
        n = len(queries)
        self.less=10**8
        self.gr = -1
        self.max_(root)
        self.min_(root)
        self.res = [[-1,-1] for i in range(n)]
        for i in range(n):
            if queries[i] >= self.less or queries[i]<=self.gr:
                self.traversal(root,queries[i],i)
        return self.res

    def traversal(self,root,query,i):
        self.min=-1
        self.max = 10**8
        self.aux_traversal(root,query)
        if self.min!=-1:
            self.res[i][0] = self.min
        if self.max!=10**8:
            self.res[i][1] = self.max
    def aux_traversal(self,root,query):
        if root!=None:
            if root.val<=query:
                if self.min == -1:
                    self.min = root.val
                elif root.val>self.min:
                    self.min = root.val
            if root.val>=query:
                if self.max == 10**8:
                    self.max = root.val
                elif root.val < self.max:
                    self.max = root.val
            if query < root.val:
                self.aux_traversal(root.left,query)
            else:
                self.aux_traversal(root.right,query)