
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        t=head
        list=[]
        j=1

        while t!=None:
            i=0
            l=[]
            while t!=None and i< j:
                l.append(t.val)
                i+=1
                t=t.next
            if len(l)%2==0:
                for i in reversed(l):
                    list.append(i)
            else:
                for i in l:
                    list.append(i)
            j+=1
        i=0
        t=head
        while t!=None:
            t.val=list[i]
            i+=1
            t=t.next
        return head



