# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self, root):
        if root == None:
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1

    def isBalanced(self, root):
        if root == None:
            return True
        return self.aux_isBalanced(root)

    def aux_isBalanced(self, root):
        if root == None:
            return True
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        if abs(left_height - right_height) > 1:
            return False
        if False in (left_height,right_height):
            return False
        return True


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BalancedBST:
    def __init__(self):
        self.root = None

    def sortedArrayToBST(self, nums):
        if not nums:
            return None

        mid = len(nums) // 2
        root = TreeNode(nums[mid])

        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])

        return root

    def insert(self, val):
        if not self.root:
            self.root = TreeNode(val)
        else:
            self.root = self._insert(self.root, val)

    def _insert(self, node, val):
        if not node:
            return TreeNode(val)

        if val < node.val:
            node.left = self._insert(node.left, val)
        else:
            node.right = self._insert(node.right, val)

        return node

    def delete(self, val):
        if not self.root:
            return
        else:
            self.root = self._delete(self.root, val)

    def _delete(self, node, val):
        if not node:
            return node

        if val < node.val:
            node.left = self._delete(node.left, val)
        elif val > node.val:
            node.right = self._delete(node.right, val)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            else:
                min_val = self._getMinValue(node.right)
                node.val = min_val
                node.right = self._delete(node.right, min_val)

        return node

    def _getMinValue(self, node):
        while node.left:
            node = node.left
        return node.val

