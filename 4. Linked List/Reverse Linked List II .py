# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        t = head
        i = 1
        list = []
        while t != None:
            if i >= left and i <= right:
                list.append(t.val)
            t = t.next
            i+=1

        j = -1
        i = 1
        t = head
        while t != None:
            if i >= left and i <= right:
                t.val = list[j]
                j -= 1
            i += 1
            t = t.next

        return head
