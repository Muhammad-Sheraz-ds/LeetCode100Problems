import random


class BinMaxHeap:
    def __init__(self, size=100) -> None:
        self.physical_size = size
        self.heap = [None] * size
        self.heapsize = 0

    def is_empty(self):
        return self.heapsize == 0

    def insert(self, val):
        self.heap[self.heapsize] = val
        self.shift_up(self.heapsize)
        self.heapsize += 1

    def Extract_Max(self):
        if self.is_empty():
            raise ('Empty Heap')
        max_val = self.heap[0]
        self.heap[0] = self.heap[self.heapsize - 1]
        self.heapsize -= 1
        self.shift_down(0)
        return max_val

    def delete(self, val):
        index = self.heap.index(val)
        self.heap[index] = self.heap[self.heapsize - 1]
        self.heapsize -= 1
        self.shift_down(index)
        self.shift_up(index)

    def increase_key(self, old, new):
        index = self.heap.index(old)
        if old >= new:
            return
        self.heap[index] = new
        self.shift_up(index)

    def get_Max(self):
        if not self.is_empty():
            return self.heap[0]
        else:
            raise ('Empty Heap')

    def shift_up(self, index):
        if index > 0:
            if self.heap[index] > self.heap[(index - 1) // 2]:
                self.heap[(index - 1) // 2],self.heap[index]=self.heap[index],self.heap[(index - 1) // 2]
                self.shift_up((index - 1) // 2)

    def shift_down(self, index):
        largest = index
        if 2 * index + 1 >= self.heapsize:
            pass
        elif self.heap[largest] < self.heap[2 * index + 1]:
            largest = 2 * index + 1
        if 2 * index + 2 >= self.heapsize:
            pass
        elif self.heap[largest] < self.heap[2 * index + 2]:
            largest = 2 * index + 2
        if largest != index:
            self.heap[largest], self.heap[index] = self.heap[index], self.heap[largest]
            self.shift_down(largest)



class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        q = BinMaxHeap()
        for i in range(len(nums)):
            q.insert(nums[0])
        for i in range(k - 1):
            q.Extract_Max()

        return q.Extract_Max()
