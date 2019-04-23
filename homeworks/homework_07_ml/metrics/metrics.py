#!/usr/bin/env python
# coding: utf-8


import numpy as np
from pandas import DataFrame as pddf


def logloss(y_true, y_pred):
    if y_true.shape != y_pred.shape:
        raise AssertionError
    return (-1/(y_true.shape[0] +
                0.00000001)) * sum(y_true*np.log(y_pred) +
                                   (1 - y_true)*np.log(1 - y_pred))


def mke_cnf_matrx(y_true, y_hat):
    matrix = np.zeros([2, 2])
    for tr, hat in zip(y_true, y_hat):
        if tr + hat == 2:
            matrix[0, 0] += 1  # [0, 0] = TP
        elif tr + hat == 0:
            matrix[1, 1] += 1  # [1, 1] = TN
        else:
            if tr == 1:
                matrix[1, 0] += 1  # [1, 0] = FN
            else:
                matrix[0, 1] += 1  # [0, 1] = FP
    return matrix


def accuracy(y_true, y_pred):
    if y_true.shape != y_pred.shape:
        raise AssertionError
    matr = mke_cnf_matrx(np.around(y_true), np.around(y_pred))
    return (matr[0, 0] + matr[1, 1])/matr.sum()


def presicion(y_true, y_pred):
    if y_true.shape != y_pred.shape:
        raise AssertionError
    matr = mke_cnf_matrx(np.around(y_true), np.around(y_pred))
    return matr[0, 0] / (matr[0, 0] + matr[0, 1])


def recall(y_true, y_pred):
    if y_true.shape != y_pred.shape:
        raise AssertionError
    matr = mke_cnf_matrx(np.around(y_true), np.around(y_pred))
    return matr[0, 0] / (matr[0, 0] + matr[1, 0])


def roc_auc(y_true, y_pred):
    if y_true.shape != y_pred.shape:
        raise AssertionError
    df = pddf({'label': y_test, 'pred': clf.predict_proba(X_test)[:, 1]})
    df = df.sort_values(by='pred', )[:: -1]
    x1 = y_test.sum()
    x2 = y_test.shape[0] - y_test.sum()
    auc = 0
    tmp = np.array([0., 0.])
    for y in df['label']:
        if y == 0:
            tmp[0] += 1 / x2
            auc += tmp[1] / x2
        else:
            tmp[1] += 1/x1
    return auc
