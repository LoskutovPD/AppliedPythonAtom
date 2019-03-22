#!/usr/bin/env python
# coding: utf-8

from multiprocessing import Process, Manager
import threading
import os


def counter(filename, counts, lock):
    x = 0
    try:
        with open(filename, "r", encoding="utf8") as f:
            for line in f:
                x += len(line.split())
    except:
        return
    lock.acquire()
    counts[filename.split("/")[-1]] = x
    lock.release()


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
    lock = threading.Lock()
    tasks = []
    counts = {}
    for file in os.listdir(path_to_dir):
        tasks.append(threading.Thread(target=counter, args=(path_to_dir + file,
                                                            counts, lock)))
        tasks[-1].start()
    for task in tasks:
        task.join()
    return counts
