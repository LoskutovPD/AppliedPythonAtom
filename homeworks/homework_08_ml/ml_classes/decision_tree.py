#!/usr/bin/env python
# coding: utf-8
import numpy as np


class Tree:
    def __init__(self, tupl=None, parent=None, left=None, right=None):
        self.tupl = tupl
        self.left = Tree(parent=self)
        self.right = Tree(parent=self)

        
class DecisionTreeClassifier:
    def __init__(self, max_depth=None, min_leaf_size=None, max_leaf_number=None, min_inform_criter=None):
        '''
        Инициализируем наше дерево
        :param max_depth: один из возможных критерием останова - максимальная глубина дерева
        :param min_leaf_size: один из возможных критериев останова - число элементов в листе
        :param max_leaf_number: один из возможных критериев останова - число листов в дереве.
        Нужно подумать как нам отобрать "лучшие" листы
        :param min_inform_criter: один из критериев останова - процент прироста информации, который
        считаем незначительным
        '''
        self.min_inform_criter = min_inform_criter
        self.min_leaf_size = min_leaf_size
        self.max_depth = max_depth
        self.max_leaf_number = max_leaf_number
        self.tree = Tree()

    def compute_split_information(self, X, y, th):
        prd = {}
        prd1, prd2 = {}, {}
        N = y.shape[0]
        N1 = 0
        for dt, lb in zip(X.squeeze(), y.squeeze()):
            try:
                prd[lb] += 1
            except KeyError:
                prd[lb] = 1
            if dt < th:
                N1 += 1
                try:
                    prd1[lb] += 1
                except KeyError:
                    prd1[lb] = 1
            else:
                try:
                    prd2[lb] += 1
                except KeyError:
                    prd2[lb] = 1
        N2 = N - N1
        gini = 1 - np.sum([(prd[t] / N)**2 for t in prd.keys()])
        gini1 = 1 - np.sum([(prd1[t] / N1)**2 for t in prd1.keys()])
        gini2 = 1 - np.sum([(prd2[t] / N2)**2 for t in prd2.keys()])
        ginis =  N1 * gini1 / N + N2 * gini2 / N
        return gini - ginis
        
    def fit(self, X, y):
        '''
        Стендартный метод обучения
        :param X: матрица объекто-признаков (num_objects, num_features)
        :param y: матрица целевой переменной (num_objects, 1)
        :return: None
        '''
        self.tree = fit_tree(X, y)
            
    def fit_tree(self, X, y):
        tree = Tree()
        if y.shape[0] <= self.min_leaf_size:
            return None
        gini_tr = 1
        mem = [-1, -1]
        for tmp in range(X.shape[1]):
            indx = np.argsort(X[:, tmp], kind='quicksort')
            array = X[indx].squeeze()[:, 1]
            lab = y[indx].squeeze()
            for j in array:
                gini = self.compute_split_information(array, lab, j)
                if gini_tr < gini:
                    gini_tr = gini
                    mem[0] = tmp
                    mem[1] = j
        if gini_tr >= min_inform_criter:
            tree.tupl = mem
            test[test[:, 1] < 2]
            tree.left = fit_tree(X[X[:, mem[0]] < mem[1]], y[[y[:, mem[0]] < mem[1]]])
            tree.right = fit_tree(X[X[:, mem[0]] >= mem[1]], y[[y[:, mem[0]] >= mem[1]]])
            return tree
    def predict(self, X):
        '''
        Метод для предсказания меток на объектах X
        :param X: матрица объектов-признаков (num_objects, num_features)
        :return: вектор предсказаний (num_objects, 1)
        '''
        pass

    def predict_proba(self, X):
        '''
        метод, возвращающий предсказания принадлежности к классу
        :param X: матрица объектов-признаков (num_objects, num_features)
        :return: вектор предсказанных вероятностей (num_objects, 1)
        '''
        pass
