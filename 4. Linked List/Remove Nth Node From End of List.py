# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional:
        if head == None or head.next == None:
            return None
        t = head
        i = 0
        while t != None:
            i += 1
            t = t.next
        sz = i
        t = head
        if n == sz:
            return head.next
        i = 0
        while t != None:
            if sz - i - 1 == n:
                t.next = t.next.next
                return head
            i += 1
            t = t.next

        return head