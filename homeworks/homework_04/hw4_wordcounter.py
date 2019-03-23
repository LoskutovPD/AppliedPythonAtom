#!/usr/bin/env python
# coding: utf-8

from multiprocessing import Process, Manager, Pool
import os


def counter(filename):
    x = 0
    try:
        with open(filename, "r", encoding="utf8") as f:
            for line in f:
                x += len(line.split())
    except:
        print("Something wrong!")
        return
    counts[filename.split("/")] = x
    counts["total"] += x


def word_count_inference(path_to_dir):
    '''
    Метод, считающий количество слов в каждом файле из директории
    и суммарное количество слов.
    Слово - все, что угодно через пробел, пустая строка "" словом не считается,
    пробельный символ " " словом не считается. Все остальное считается.
    Решение должно быть многопроцессным. Общение через очереди.
    :param path_to_dir: путь до директории с файлами
    :return: словарь, где ключ - имя файла, значение - число слов +
        специальный ключ "total" для суммы слов во всех файлах
    '''
    pl = Pool()
    counts = Manager.dict()
    counts["total"] = 0
    pl.map(counter, os.listdir(path_to_dir))
    pl.close()
    pl.join()
    return counts
