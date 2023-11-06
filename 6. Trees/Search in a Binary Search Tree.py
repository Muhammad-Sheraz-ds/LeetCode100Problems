# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        self.v = None
        self.search(root, val)
        return self.v

    def search(self, root, val):
        if root != None:
            if root.val == val:
                self.v = root
                return
            left = self.search(root.left, val)
            right = self.search(root.right, val)

