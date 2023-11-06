# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l = []
        t=head
        while t!=None:
            l.append(t.val)
            t=t.next
        i=len(l)-1
        t = head
        while t != None:
            if l[i]!=t.val:
                return False
            t = t.next
            i-=1
        return True