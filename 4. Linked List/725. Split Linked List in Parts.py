class Solution:
    def splitListToParts(self, head: ListNode, k: int) -> List[ListNode]:
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next

        part_size = length // k
        extra = length % k

        result = []
        temp = head
        for i in range(k):
            result.append(temp)

        part_size = length // k
        extra = length % k

        result = []
        temp = head
        for i in range(k):
            result.append(temp)



    def splitListToParts(self, head, k):
        t = head
        n=0
        while t != None:
            t = t.next
            n += 1
        ans = [None] * k
        extra = n % k
        parts = n // k
        j = 0
        while j < k:
            i = parts
            if extra != 0:
                i += 1
                extra -= 1
            t = head
            while True:
                if i == 1:
                    break
                t = t.next
                i -= 1
            if t:
                head = t.next
                t.next = None
            ans[j] = head
            j += 1











