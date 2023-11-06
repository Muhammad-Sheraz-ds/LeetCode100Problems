class Queue:
    def __init__(self) -> None:
        self.head = self.Node()
        self.tail = self.Node(None, self.head, self.head)
        self.head.next = self.tail
        self.size = 0

    class Node:
        def __init__(self, data=None, prev=None, next=None):
            self.data = data
            self.prev = prev
            self.next = next

    def enqueue(self, obj):
        tmp = self.Node(obj, self.tail.prev, self.tail)
        self.tail.prev.next = tmp
        self.tail.prev = tmp
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise ('Empty')
        t = self.tail.prev
        t.prev.next = self.tail
        self.tail.prev = t.prev
        self.size -= 1
        return t.data

    def is_empty(self):
        return self.size == 0


class MyStack:
    def __init__(self):
        self.q1=Queue()
        self.q2=Queue()


    def push(self, x: int) -> None:
        self.q1.enqueue(x)
        self.q2.enqueue(x)

    def pop(self) -> int:
        return self.q2.dequeue()


    def top(self) -> int:
        return self.q2.tail.prev.data

    def empty(self) -> bool:
        return self.q2.is_empty()