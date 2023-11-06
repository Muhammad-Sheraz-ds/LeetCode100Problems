# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        t=head
        list = []
        while t != None:
            list.append(t.val)
            t = t.next

        j = -1
        t = head
        while t != None:
            t.val = list[j]
            j -= 1
            t = t.next

        return head
