class Solution:
    def max_index(self, array, n):
        m = 0
        v = array[0]
        for i in range(0, n):
            if array[i] > v:
                m = i
                v = array[i]
        return m

    def constructMaximumBinaryTree(self, nums):
        return self.auxtraversal(nums)

    def auxtraversal(self, nums):
        n = len(nums)
        if n == 0:
            return None
        i = self.max_index(nums, n)
        root = TreeNode(nums[i])
        root.left = self.auxtraversal(nums[0:i])
        root.right = self.auxtraversal(nums[i + 1:n])
        return root