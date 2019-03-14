#!/usr/bin/env python
# coding: utf-8

from .heap import MaxHeap


class UpdateMaxHeap(MaxHeap):
    def __init__(self, array):
        super(UpdateMaxHeap, self).__init__(array)

    def extract_maximum(self):
        if self.heap_size == 0:
            return None
        maximum = self.array[0][-1]
        if len(self.array[0]) == 1:
            self.array[0] = self.array[self.heap_size - 1]
            self.heap_size -= 1
            self._heapify(0)
        else:
            self.array[0] = self.array[0][:-1]
            self._heapify(0)
        return maximum

    def _heapify(self, index):
        largest = index
        if 2 * index + 1 <= self.heap_size - 1:
            if self.array[2 * index + 1][-1] > self.array[largest][-1]:
                largest = 2 * index + 1
        if 2 * index + 2 <= self.heap_size - 1:
            if self.array[2 * index + 2][-1] > self.array[largest][-1]:
                largest = 2 * index + 2
        if self.array[largest] != self.array[index]:
            self.array[index], self.array[largest] = \
                self.array[largest], self.array[index]
            self._heapify(largest)


class FastSortedListMerger:

    @staticmethod
    def merge_first_k(list_of_lists, k):
        heap = UpdateMaxHeap(list_of_lists)
        return [heap.extract_maximum() for i in range(k)]
