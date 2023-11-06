# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less = []
        gr = []
        e=[]
        l = less+e+gr
        t = head
        while t != None:
            if t.val < x:
                less.append(t.val)
            else:
                e.append(t.val)
            t=t.next
        t = head
        i=0
        while t != None:
            t.val = l[i]
            i+=1
            t=t.next
        return head

