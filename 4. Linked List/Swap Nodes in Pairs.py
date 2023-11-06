#Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        if node == None:
            return None
        elif node.next == None:
            return node
        elif node.next.next == None:
            tmp = ListNode(node.next.val, ListNode(node.val))
            return tmp
        head = ListNode(head.next.val, ListNode(head.val,head.next.next))
        t = head
        t = t.next
        while t!=None and t.next!=None and t.next.next != None:
            tmp = t.next.val
            t.next=t.next.next
            t.next.next = ListNode(tmp,t.next.next)
            t = t.next.next
        return head










