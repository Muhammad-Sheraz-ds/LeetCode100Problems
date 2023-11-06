class Solution:
    def isSubtree(self, root, subRoot):
        return self.traverse(root,subRoot)

    def traverse(self,root,sub_root):
        if root!=None:
            ans=False
            if root.val==sub_root.val:
                ans = self.isSameTree(root,sub_root)
            if ans:
                return True
            s1 = self.traverse(root.left,sub_root)
            s2 = self.traverse(root.right,sub_root)
            if s1==True or s2== True:
                return True
            return False
        return False

    def isSameTree(self, p, q):
        if p == q == None:
            return True
        elif p == None or q == None:
            return False
        return self.aux_traversal(p, q)

    def aux_traversal(self, p, q):
        if p == q == None:
            return True
        elif p == None or q == None:
            return False
        elif p.val != q.val:
            return False
        s1 = self.aux_traversal(p.left, q.left)
        s2 = self.aux_traversal(p.right, q.right)
        if s1 == False or s2 == False:
            return False
        return True