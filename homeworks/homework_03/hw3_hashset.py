#!/usr/bin/env python
# coding: utf-8

from homeworks.homework_03.hw3_hashmap import HashMap


class HashSet(HashMap):
    class Entry(HashMap.Entry):
        def __init__(self, key):
            self.key = key
            self.next_v = None

    def __init__(self):
        super(HashSet, self).__init__()

    def get(self, key):
        return key in self.keys()

    def put(self, key):
        tmp = self.entries[self._get_index(self._get_hash(key))]
        if tmp is None:
            tm = self.Entry(key)
            self.entries[hash(key) % self.buckets] = tm
            self.len += 1
            return True
        while tmp is not None:
            if tmp.key == key:
                return False
            if tmp.next_v is None:
                tmp.next_v = self.Entry(key)
                self.len += 1
                return True
            tmp = tmp.next_v

    def values(self):
        # TODO возвращать итератор значений
        return self.keys()

    def intersect(self, another_hashset):
        # TODO метод, возвращающий новый HashSet
        #  элементы - пересечение текущего и другого
        return [key for key in self.keys() if key in another_hashset.keys()]
