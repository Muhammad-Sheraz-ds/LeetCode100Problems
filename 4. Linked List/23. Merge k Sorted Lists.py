class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return None

        self.k = len(lists)
        self.res = None
        self.lists = lists
        self.size = self.k

        while True:
            min_val = float('inf')
            min_index = -1

            for i in range(self.k):
                if self.lists[i] and self.lists[i].val < min_val:
                    min_val = self.lists[i].val
                    min_index = i

            if min_index == -1:
                return self.res

            if self.res is None:
                self.res = ListNode(min_val)
                self.current = self.res
            else:
                self.current.next = ListNode(min_val)
                self.current = self.current.next

            self.lists[min_index] = self.lists[min_index].next
