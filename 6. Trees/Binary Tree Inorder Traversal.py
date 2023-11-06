class Solution:
    def inorderTraversal(self, root):
        ans=[]
        self.aux_inorderTraversal(root,ans)
        return ans
    def aux_inorderTraversal(self, root,ans):
        if root!=None:
            self.aux_inorderTraversal(root.left)
            ans.append(root.value)
            self.aux_inorderTraversal(root.right)








'''# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    list=[]
    def inorderTraversal(self, root):
        self.aux_inorderTraversal(root,0,len(root))
        return Solution.list
    def aux_inorderTraversal(self, root,i,n):
        if i < n and root[i]!=None:
            self.aux_inorderTraversal(root, 2*i+1, n)
            Solution.list.append(root[i])
            self.aux_inorderTraversal(root, 2*i+2, n)


'''