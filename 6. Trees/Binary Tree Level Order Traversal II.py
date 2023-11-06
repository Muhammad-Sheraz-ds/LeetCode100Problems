# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root):
        if root==None:
            return []
        self.levels = self.aux_levels(root, 0)
        self.res = [[] for j in range(self.levels+1)]
        self.aux_inorderTraversal(root,0)
        return self.res

    def aux_levels(self,root, levels):
        if root != None:
            if root.left == None and root.right == None:
                return levels
            s1 = self.aux_levels(root.left, levels + 1)
            s2 = self.aux_levels(root.right, levels + 1)
            return max(s1,s2)
        return levels


    def aux_inorderTraversal(self, root, levels):
        if root != None:
            self.res[self.levels-levels].append(root.val)
            self.aux_inorderTraversal(root.left, levels+1)
            self.aux_inorderTraversal(root.right, levels+1)

