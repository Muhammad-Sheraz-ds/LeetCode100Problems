class Node:
    def __init__(self, val, ind, next=None):
        self.val = val
        self.ind = ind
        self.next = next


class Linked_list:
    def display(self):
        l=self.head
        while l:
            print(l.val)
            l=l.next

    def __init__(self):
        self.head = None
        self.tail = None

    def get_list(self, k):
        l = []
        t = self.head
        while t and k > 0:
            k -= 1
            print(t.val)
            l.append(t.ind)
            t = t.next
        return l

    def append(self, val, ind):
        if self.head == None:
            self.head = Node(val, ind)
            self.tail = self.head

        elif self.head.val > val:
            self.head = Node(val, ind, self.head)
        elif self.tail.val < val:
            self.tail.next = Node(val, ind)
            self.tail = self.tail.next
        elif self.tail.val == val:
            self.tail.next = Node(val, ind)
            self.tail = self.tail.next
        else:
            t = self.head
            while t.next:
                if t.next.val == val:
                    n = Node(val, ind)
                    tmp = t.next.next
                    t.next.next = n
                    n.next = tmp
                    break

                elif t.next.val > val:
                    n = Node(val, ind)
                    n.next = t.next
                    t.next = n
                    break
                t=t.next


class Solution:
    def kWeakestRows(self, mat, k):
        r = len(mat)
        col = len(mat[0])
        l = Linked_list()
        i = 0
        while i < r:
            j = 0
            c = 0
            while j < col and mat[i][j] == 1:
                c += 1
                j += 1
            l.append(c, i)
            i += 1
        #return l.display()
        return l.get_list(k)




s=Solution()
ans = s.kWeakestRows([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[1,1,1,0],[0,0,0,0]],3)
print(ans)