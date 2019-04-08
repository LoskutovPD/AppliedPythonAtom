#!/usr/bin/env python
# coding: utf-8


<<<<<<< HEAD
def groupping_anagramms(words):
=======
def groupping_anagramms(list_w):
>>>>>>> master
    """
    Функция, которая группирует анаграммы.
    Возвращаем массив, где элементом является массив с анаграмами.
    Пример:  '''Аз есмь строка живу я мерой остр
                За семь морей ростка я вижу рост
                Я в мире сирота
                Я в Риме Ариост'''.split()
                ->
                [
                 ['Аз'], ['есмь', 'семь'],
                 ['строка', 'ростка'], ['живу', 'вижу'],
                 ['я', 'я'], ['мерой', 'морей'],
                 ['остр)'], ['За'], ['рост'], ['Я', 'Я'],
                 ['в', 'в'], ['мире'], ['сирота'],
                 ['Риме'], ['Ариост']
                ]
    :param words: list of words (words in str format)
    :return: list of lists of words
    """
    # TODO: реализовать функцию
<<<<<<< HEAD
    raise NotImplementedError
=======
    final_dict, sets = [], []
    for x in range(len(list_w)):
        if set(list_w[x].lower()) in sets:
            final_dict[sets.index(set(list_w[x].lower()))].append(list_w[x])
        else:
            sets.append(set(list_w[x].lower()))
            final_dict.append([list_w[x]])
    return final_dict
>>>>>>> master
