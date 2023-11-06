# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root):
        self.aux_inorderTraversal(root,0)
    def aux_inorderTraversal(self, root,ans):
        if root!=None:
            s1,s2=0,0
            if root.left != None and root.left.val==root.val:
                s1=self.aux_inorderTraversal(root.left,ans+1)
            else:
                s1=self.aux_inorderTraversal(root.left,0)
            if root.right != None and root.right.val==root.val:
                s2=self.aux_inorderTraversal(root.right,ans+1)
            else:
                s2=self.aux_inorderTraversal(root.right,0)
            return max(s1,s2)

        return 0




