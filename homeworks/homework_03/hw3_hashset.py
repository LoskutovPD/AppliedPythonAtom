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

    def get(self, key, default_value=None):
        tmp = self.entries[hash(key) % self.buckets]
        if tmp is None:
            return default_value
        else:
            while tmp is not None:
                if tmp.key == key:
                    return tmp.key
                if tmp.next_v is None:
                    return default_value
                tmp = tmp.next_v

    def put(self, key):
        return key in self

    def values(self):
        # TODO возвращать итератор значений
        return self.keys()

    def intersect(self, another_hashset):
        # TODO метод, возвращающий новый HashSet
        #  элементы - пересечение текущего и другого
        return [key for key in self.keys() if key in another_hashset.keys()]
