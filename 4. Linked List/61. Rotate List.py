# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        l = []
        temp = head
        while temp:
            l.append(temp.val)
            temp = temp.next
        temp = head
        n=len(l)
        if k==0 or n==0:
            return head
        k=k%n
        i=0
        while temp:
            temp.val = l[i-k]
            temp = temp.next
            i+=1

        return head