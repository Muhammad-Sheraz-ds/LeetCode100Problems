class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        self.l1 = l1
        self.l2 = l2
        self.res = ListNode()
        ans = self.res
        p=self.l1
        q=self.l2
        self.p=0
        carry=0
        self.q=0
        while True:
            if p==None and q==None:
                if carry != 0:
                    ans = ListNode(carry)
                return
            s=0
            if p!=None:
                s+=p.val
                p=p.next
            if q!=None:
                s+=q.val
                q=q.next
            if s> 9:
                carry=s%10
                s=s//10
            ans.val = s
            ans = ans.next
        return self.res


