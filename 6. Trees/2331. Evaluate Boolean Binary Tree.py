class Solution:
    def evaluateTree(self, root) -> bool:
        return self.evaluate(root)

    def evaluate(self, rt):
        if rt.val == 0:
            return False
        if rt.val == 1:
            return True
        if rt.val == 2:
            return self.evaluate(rt.right) or self.evaluate(rt.left)
        if rt.val == 3:
            return self.evaluate(rt.right) and self.evaluate(rt.left)


