#!/usr/bin/env python
# coding: utf-8
import copy


class Heap(object):

    def __init__(self, array):
        self.array = copy.deepcopy(array)
        self.heap_size = 0
        self.build_heap()

    def add(self, elem_with_priority):
        self.heap_size += 1
        self.array.append((-2147483658, -2147483658))
        self._increase_key(self.heap_size - 1, elem_with_priority)

    def _increase_key(self, index, key):
        if key >= self.array[index]:
            self.array[index] = key
            while index > 0 and self.array[index // 2] < self.array[index]:
                self.array[index], self.array[index // 2] = \
                    self.array[index // 2], self.array[index]
                index //= 2

    def build_heap(self):
        self.heap_size = len(self.array)
        [self._heapify(i) for i in range(len(self.array) - 1, -1, -1)]

    def _heapify(self, index):
        largest = index
        if len(self.array[index]) == 0:
            self.array[0] = [-2147483658]
        if 2 * index + 1 <= self.heap_size - 1:
            if comparator_d(self.array[2 * index + 1], self.array[largest]):
                largest = 2 * index + 1
        if 2 * index + 2 <= self.heap_size - 1:
            if comparator_d(self.array[2 * index + 2], self.array[largest]):
                largest = 2 * index + 2
        if self.array[largest] != self.array[index]:
            self.array[index], self.array[largest] = \
                self.array[largest], self.array[index]
            self._heapify(largest)

    def _heap_sort(self):
        self.build_heap()
        for i in range(len(self.array) - 1, -1, -1):
            self.array[0], self.array[i] = self.array[i], self.array[0]
            self.heap_size -= 1
            self._heapify(0)


class MaxHeap(Heap):

    def __init__(self, array):
        super(MaxHeap, self).__init__(array)

    def extract_maximum(self):
        if self.heap_size == 0:
            return None
        maximum = self.array[0]
        self.array[0] = self.array[self.heap_size - 1]
        self.heap_size -= 1
        self._heapify(0)
        return maximum


def comparator_d(x, y):
    if x[0] == y[0]:
        return x[1] >= y[1]
    elif x[0] > y[0]:
        return True
    else:
        return False
