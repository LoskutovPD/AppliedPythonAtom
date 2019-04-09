#!/usr/bin/env python
# coding: utf-8

import numpy as np


def simplex_method(a, b, c):
    """
    Почитать про симплекс метод простым языком:
    * https://  https://ru.wikibooks.org/wiki/Симплекс-метод._Простое_
    объяснение
    Реализацию алгоритма взять тут:
    * https://youtu.be/gRgsT9BB5-8 (это ссылка на 1-ое из 5 видео).

    Используем numpy и, в целом, векторные операции.

    a * x.T <= b
    c * x.T -> max
    :param a: np.array, shape=(n, m)
    :param b: np.array, shape=(n, 1)
    :param c: np.array, shape=(1, m)
    :return x: np.array, shape=(1, m)
    """
    ans = np.zeros_like(c) - 1
    eye = np.eye(a.shape[0]+1)
    b1 = b.reshape((b.shape[0], 1))
    b1 = np.concatenate([b1, [[0]]])
    a1 = np.concatenate([a, [c*(-1)]])
    m = np.concatenate([a1, eye, b1], axis=1)
    return solve(m, ans)


def solve(m, ans):
    piv = pivot(m)
    m[piv[0]] = m[piv[0]]/m[piv]
    for i in range(len(m)):
        if i != piv[0]:
            m[i] = m[i] - m[piv[0]]*m[i, piv[1]]
    if piv[0] in ans:
        for l in range(len(ans)):
            if ans[l] == piv[0]:
                ans[l] = -1
    ans[piv[1]] = piv[0]
    if m[-1].min() >= 0:
        res = np.zeros(ans.shape[0])
        print(ans, res)
        for i in range(len(ans)):
            if ans[i] > -1:
                res[i] = m[ans[i], -1]
        return res
    else:
        return solve(m, ans)


def pivot(m):
    tmp = m[-1]
    ll = tmp.min()
    for x in range(len(tmp)):
        if tmp[x] == ll:
            ll = x
            break
    n = 10**10
    ind = 0
    for x in range(0, len(m) - 1):
        if n > (m[x, -1] / m[x, ll]):
            n = m[x, -1] / m[x, ll]
            ind = x
    return ind, ll
