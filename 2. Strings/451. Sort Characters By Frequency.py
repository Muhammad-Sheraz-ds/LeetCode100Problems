class Solution:
    class Linked_list:
        class Node:
            def __init__(self, val, alphabet, next=None):
                self.alphabet = alphabet
                self.next = next
                self.val = val
        class Iterator:
            def __init__(self,lt):
                self.current = lt.list
            def __iter__(self):
                return self

            def __next__(self):
                if self.current!=None:
                    val = self.current.alphabet,self.current.val
                    self.current=self.current.next
                    return val
                else:
                    raise StopIteration
        def __init__(self):
            self.list = None

        def __iter__(self):
            return self.Iterator(self)
        def append(self,val,alphabet):
            if self.list==None:
                self.list=self.Node(val,alphabet)
                return
            if self.list.val<val:
                self.list = self.Node(val,alphabet,self.list)
                return
            nd = self.Node(val,alphabet)
            t=self.list
            while t.next!=None:
                if t.next.val<val:
                    break
                t=t.next
            nd.next = t.next
            t.next = nd
    def frequencySort(self, s):
            d = dict()
            for i in s:
                try:
                    d[i] += 1
                except:
                    d[i] = 1
            list = self.Linked_list()
            for key in d.keys():
                list.append(d[key],key)
            l = ''
            for i in list:
                l += i[0] * i[1]
            return l




