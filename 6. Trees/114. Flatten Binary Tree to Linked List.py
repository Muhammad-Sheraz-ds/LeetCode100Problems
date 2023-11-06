class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        self.travrese(root)

    def travrese(self,root):
        if root!=None:
            if root.left!=None:
                t = root.left
                while t.right:
                    t = t.right
                t.right = root.right
                root.right = root.left
                root.left =None

            self.travrese(root.right)


