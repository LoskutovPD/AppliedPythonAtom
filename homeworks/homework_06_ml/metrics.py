#!/usr/bin/env python
# coding: utf-8


import numpy as np


def mse(y_true, y_hat, derivative=False):
    if y_true.shape != y_hat.shape:
        raise AssertionError
    return sum((y_true - y_hat)**2) / y_true.shape[0]


def mae(y_true, y_hat):
    if y_true.shape != y_hat.shape:
        raise AssertionError
    return sum(np.abs(y_true - y_hat)) / y_true.shape[0]


def r2_score(y_true, y_hat):
    y = sum(y_true)/y_true.shape[0]
    return 1 - mse(y_true, y_hat)*y_true.shape[0]/sum((y_true - y)**2)
