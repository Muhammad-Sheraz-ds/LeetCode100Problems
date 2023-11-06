# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root) -> List[int]:
        self.ans = []
        d = {}
        self.traversal(root)
        m = 0
        self.a = []
        for i in self.ans:
            try:
                d[i] += 1
            except:
                d[i] = 1
            if d[i] > m:
                m = d[i]
        for key in d.keys():
            if d[key] == m:
                self.a.append(key)
        return self.a

    def traversal(self, rt):
        if rt != None:
            if rt.left != None:
                self.traversal(rt.left)
            self.ans.append(rt.val)
            if rt.right != None:
                self.traversal(rt.right)
