#!/usr/bin/env python
# coding: utf-8
import numpy as np
import pandas as pd


class KNNRegressor:
    def __init__(self, n):
        self.n = n

    def fit(self, X, y):
        self.X = X
        self.y = y

    def predict(self, inp):
        y = []
        assert len(inp.shape) == 2
        for t in inp:
            # Посчитаем расстояние от всех элементов в тренировочной выборке
            # до текущего примера -> результат - вектор размерности трейна
            d = np.sqrt(((self.X - t)**2).sum(axis=1))
            # Возьмем индексы n элементов, расстояние до которых минимально
            # результат -> вектор из n элементов
            idx = np.argsort(d)[:self.n]
            # TODO
            prediction = np.mean(self.y[idx])
            y.append(prediction)
        return y
