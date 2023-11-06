class Solution:
    def findBottomLeftValue(self, root):
        if root == None:
            return []
        self.ans=None
        self.levels = self.aux_levels(root, 0)
        self.aux_inorderTraversal(root,0)
        return self.ans

    def aux_levels(self, rt, levels):
        if rt != None:
            s1 = self.aux_levels(rt.left, levels + 1)
            s2 = self.aux_levels(rt.right, levels + 1)
            return max(s1, s2)
        return levels

    def aux_inorderTraversal(self, rt, level):
        if rt != None:
            if self.levels==level and self.ans==None:
                self.ans = rt.val
                return
            self.aux_inorderTraversal(rt.left, level + 1)
            self.aux_inorderTraversal(rt.right, level + 1)
