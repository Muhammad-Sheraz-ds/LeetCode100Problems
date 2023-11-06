# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root):
        self.paths =[]
        self.aux_inorderTraversal(root,'')
        return self.paths
    def aux_inorderTraversal(self, root ,ans):
        if root !=None:
            if root.left==root.right==None:
                ans += str(root.val)
                self.paths.append(ans)
            ans +=str(root.val) +'->'
            self.aux_inorderTraversal(root.left,ans)
            self.aux_inorderTraversal(root.right,ans)





'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root):
        self.paths=[]
        self.aux_inorderTraversal(root,'')
        return self.paths
    def aux_inorderTraversal(self, root,ans):
        if root!=None:
            ans+=str(root.val)+'->'
            self.aux_inorderTraversal(root.left,ans)
            self.aux_inorderTraversal(root.right,ans)
        else:
            if len(ans)!=0:
                self.paths.append(ans[0:-1])


'''