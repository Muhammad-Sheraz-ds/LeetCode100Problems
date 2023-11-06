# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        t=head
        list=[]
        while t!=None:
            i=0
            l=[]
            while t!=None and i< k:
                l.append(t.val)
                i+=1
                t=t.next
            if i == k:
                for i in reversed(l):
                    list.append(i)
            else:
                for i in l:
                    list.append(i)
        i=0
        t=head
        while t!=None:
            t.val=list[i]
            i+=1
            t=t.next
        return head



