# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        self.levels = self.aux_levels(root, 0)
        self.res = [[]for j in range(self.levels + 1)]
        self.aux_inorderTraversal(root, 0)
        l = []
        for i in self.res:
            if i!=[]:
                l.append(i[-1])
        return l




    def aux_levels(self, rt, levels):
        if rt != None:
            if rt.left == None and rt.right == None:
                return levels
            s1 = self.aux_levels(rt.left, levels + 1)
            s2 = self.aux_levels(rt.right, levels + 1)
            return max(s1, s2)
        return levels

    def aux_inorderTraversal(self, rt, levels):
        if rt != None:
            self.res[levels].append(rt.val)
            self.aux_inorderTraversal(rt.left, levels + 1)
            self.aux_inorderTraversal(rt.right, levels + 1)


