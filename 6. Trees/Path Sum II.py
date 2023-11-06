class Solution:
    def pathSum(self, root, targetSum):
        self.target = targetSum
        self.res = []
        self.aux_inorderTraversal(root, 0, [])
        return self.res

    def aux_inorderTraversal(self, root, ans, path):
        if root is not None:
            if root.left is None and root.right is None:
                ans += root.val
                path.append(root.val)
                if ans == self.target:
                    self.res.append(path[:])  # Append a copy of the path
            self.aux_inorderTraversal(root.left, ans + root.val, path + [root.val])
            self.aux_inorderTraversal(root.right, ans + root.val, path + [root.val])