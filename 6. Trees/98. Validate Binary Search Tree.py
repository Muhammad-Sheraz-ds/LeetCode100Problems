
class Solution:
    def isValidBST(self, root) -> bool:
        self.traversal(root)
    def traversal(self, rt):
        if rt != None:
            s1 = self.traversal(rt.left)
            s2 = self.traversal(rt.right)
            if rt.left!=None and rt.val > rt.left:
                s1=True
            if rt.right != None and rt.val > rt.left:

        return True