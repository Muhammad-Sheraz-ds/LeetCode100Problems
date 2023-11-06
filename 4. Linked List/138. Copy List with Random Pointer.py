class Node:
    def __init__(self, val, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

def copyRandomList(head):
    if not head:
        return None

    # Step 1: Creating a copy of each old node and insert it next to the old node it's copied from.
    # This will create new alternative nodes which are a copy (except random pointer) of its previous node.
    node = head
    while node:
        temp = node.next
        node.next = Node(node.val)
        node.next.next = temp
        node = temp

    # Step 2: Copy the random pointer (if exists) of the old nodes to their copy new nodes.
    node = head
    while node:
        if node.random:
            node.next.random = node.random.next
        node = node.next.next  # Go to the next old node

    # Step 3: Copy the alternative nodes into the "ans" linked list using the "helper" pointer
    # along with restoring the old linked list.
    ans = Node(0)  # The first node is a dummy node
    helper = ans

    while head:
        # Copy the alternate added nodes from the old linked list
        helper.next = head.next
        helper = helper.next

        # Restoring the old linked list by removing the alternative newly added nodes
        head.next = head.next.next
        head = head.next  # Go to the next alternate node

    return ans.next  # Since the first node is a dummy node
