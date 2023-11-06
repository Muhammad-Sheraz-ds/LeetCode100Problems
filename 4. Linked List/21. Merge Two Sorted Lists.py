class Solution:
    def mergeTwoLists(self, list1, list2):
        self.ans = None
        if list1==None and list2==None:
            return None
        if list1==None:
            return list2
        if list2 ==None:
            return list1
        self.aux_traverse(list1,list2)
        return self.ans

    def aux_traverse(self, list1, list2):
        if list1==None and list2==None:
            return
        if list1==None:
            self.current.next = list2
        elif list2 ==None:
            self.current.next = list1
        else:
            if list1.val < list2.val:
                if self.ans==None:
                    self.ans=ListNode(list1.val)
                    self.current = self.ans


                else:
                    self.current.next = ListNode(list1.val)
                    self.current=self.current.next
                self.aux_traverse(list1.next,list2)
            else:
                if self.ans == None:
                    self.ans = ListNode(list2.val)
                    self.current=self.ans
                else:
                    self.current.next = ListNode(list2.val)
                    self.current=self.current.next
                self.aux_traverse(list1,list2.next)


