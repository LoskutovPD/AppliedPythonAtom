#!/usr/bin/env python
# coding: utf-8


def revert_linked_list(head):
    """
    A -> B -> C should become: C -> B -> A
    :param head: LLNode
    :return: new_head: LLNode
    """
    # TODO: реализовать функцию
<<<<<<< HEAD
    raise NotImplementedError
=======
    return revert(head.next_node, head)


def revert(next_v, prev=None):
    if next_v is None:
        return prev
    next_v.next_node, tmp = prev, next_v.next_node
    return revert(tmp, next_v)
>>>>>>> master
