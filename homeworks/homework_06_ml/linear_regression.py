#!/usr/bin/env python
# coding: utf-8
from metrics import mse, r2_score, mae
import numpy as np


class LinearRegression:
    def __init__(self, lambda_coef=1.0, regulatization=None, alpha=0.5):
        self.lambda_coef = lambda_coef
        self.regulatization = regulatization
        self.alpha = alpha
        self.trained = False
        self.W = np.random.rand(1)
        self.b = np.random.rand(1)

    def fit(self, X_train, y_train, iteration=100):
        if X_train.shape[0] != y_train.shape[0]:
            raise AssertionError
        stop = 0
        for i in range(iteration):
            grad = self._grad(X_train.T[0], y_train)
            self.W -= self.lambda_coef * grad[0]
            self.b -= self.lambda_coef * grad[1]
            y_hat = grad[2]
            mseloss = mse(y_hat, y_train)
            r2loss = r2_score(y_train, y_hat)
            maeloss = mae(y_hat, y_train)
            if np.abs(stop - r2loss) < 0.00001
                break
            stop = r2loss
            if i % 10 == 0:
                print(f"Iteration:{i}\nmseloss: {mseloss}, r2loss: {r2loss}, maeloss: {maeloss}")
        self.trained = True

    def _grad(self, x_train, y_true):
        y_hat = self.W.T * x_train + self.b
        if self.regulatization == "L2":
            tmp = np.linalg.norm(self.W, ord=1) * self.lambda_coef
        elif self.regulatization == "L1":
            tmp = np.linalg.norm(self.W) * 2 * self.lambda_coef
        else:
            tmp = 0
        dW = tmp + (-1) * sum((2 * x_train *
                               (y_true - y_hat).T))/y_true.shape[0]
        db = (-1) * sum((2 *
                         (y_true - y_hat).T))/y_true.shape[0]
        return dW, db, y_hat

    def predict(self, X_test):
        if not self.trained:
            raise AssertionError
        return X_test * self.W.T + self.b

    def get_weights(self):
        if not self.trained:
            raise NotTrainingError
        return self.W, self.b
