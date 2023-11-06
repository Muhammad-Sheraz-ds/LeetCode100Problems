# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        self.depth=depth
        self.val=val
        if depth==1:
            root = TreeNode(self.val,root)
            return root
        self.iterate(root,1)
        return root

    def iterate(self,root,level):
        if root==None or level>=self.depth:
            return
        if level==self.depth-1:
            r,l = TreeNode(self.val,None,root.right),TreeNode(self.val,root.left)
            root.right = r
            root.left=l
        self.iterate(root.right,level+1)
        self.iterate(root.left,level+1)
