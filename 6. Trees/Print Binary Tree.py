
lass Solution:
    def printTree(self, root):
        if root == None:
            return []
        self.levels = self.aux_levels(root, 0)+1
        self.h = self.levels
        self.w = self.levels+1
        self.res = [['' for i in range(self.levels+1)] for j in range(self.levels)]
        i,j= 0,(self.levels - 1) // 2
        self.aux_inorderTraversal(root,i,j)
        return self.res

    def aux_levels(self, root, levels):
        if root != None:
            if root.left == None and root.right == None:
                return levels
            s1 = self.aux_levels(root.left, levels + 1)
            s2 = self.aux_levels(root.right, levels + 1)
            return max(s1, s2)
        return levels

    def aux_inorderTraversal(self, root, i,j):
        if root != None:
            self.res[i][j] = str(root.val)
        self.aux_inorderTraversal(root.left,i+1,j+(2**(self.h-i-1)))
        self.aux_inorderTraversal(root.right, i+1, j-(2**(self.h-i-1)))



