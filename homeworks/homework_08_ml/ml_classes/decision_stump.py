#!/usr/bin/env python
# coding: utf-8
import numpy as np


class DecisionStumpRegressor:
    def __init__(self):
        self.th = None
        self.yl = None
        self.yr = None

    def fit(self, X, y):
        indx = np.argsort(X).squeeze()
        data = X.T[indx].T
        label = y.T[indx].T
        self.th = data[0, 1]
        our_loss = self.loss(label[0, :1]) + self.loss(label[0, 1:])
        for tmp in range(2, data.shape[1] - 1):
            if self.loss(label[0, :tmp]) + self.loss(label[0, tmp:]) < our_loss:
                our_loss = self.loss(label[0, :tmp]) + self.loss(label[0, tmp:])
                self.th = data[0, tmp]
        self.y1 = label[0, :self.th].mean()
        self.y2 = label[0, self.th:].mean()

    def loss(self, y):
        return ((y - y.mean())**2).sum() / y.shape[0]

    def predict(self, X):
        pred = []
        for tmp in X[0]:
            if tmp < self.th:
                pred.append(self.y1)
            else:
                pred.append(self.y2)
        return pred
    
