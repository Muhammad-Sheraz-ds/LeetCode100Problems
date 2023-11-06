class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowestCommonAncestor(root, p, q):
    while root:
        # If both nodes have smaller values than the root, go left
        if root.val > p.val and root.val > q.val:
            root = root.left
        # If both nodes have larger values than the root, go right
        elif root.val < p.val and root.val < q.val:
            root = root.right
        else:
            break
    return root
