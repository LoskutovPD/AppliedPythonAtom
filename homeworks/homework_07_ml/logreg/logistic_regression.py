#!/usr/bin/env python
# coding: utf-8


import numpy as np


class LogisticRegression:
    def __init__(self, lambda_coef=1.0, regulatization=None,
                 c=2, n_iter=100):
        self.lambda_coef = lambda_coef
        self.regul = regulatization
        self.alpha = 1 / c
        self.iter = n_iter
        self.train = False

    def fit(self, X_train, y_train):
        self.train = True
        label = np.array([y_train.T]).T
        self.w = np.random.randn(X_train.shape[1], 1)
        if self.regul == "L2":
            tmp = np.linalg.norm(self.w, ord=1) * self.lambda_coef
        elif self.regul == "L1":
            tmp = np.linalg.norm(self.w) * 2 * self.lambda_coef
        else:
            tmp = 0
        for _ in range(self.iter):
            pred = self.predict_proba(X_train)
            grad = self.alpha * tmp + ((X_train.T @ (pred - label)) /
                                       X_train.shape[0])
            self.w -= grad * self.lambda_coef

    def predict(self, X):  # around
        assert self.train, 'dummy attempt'
        return np.around(self.predict_proba(X))

    def predict_proba(self, X):  # sigmoid
        assert self.train, 'dummy attempt'
        tpm = -X @ self.w
        return 1 / (1 + np.exp(tpm))

    def get_weights(self):
        assert self.train, 'dummy attempt'
        return self.w
