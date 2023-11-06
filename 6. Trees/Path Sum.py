# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root, target):
        self.target=target
        return self.aux_inorderTraversal(root,0)
    def aux_inorderTraversal(self, root ,ans):
        if root !=None:
            ans += root.val
            if root.left==root.right==None:
                if ans== self.target:
                    return True
            s1 = self.aux_inorderTraversal(root.left,ans)
            s2 = self.aux_inorderTraversal(root.right,ans)
            if s1==True or s2==True:
                return True
            return False
        return False

