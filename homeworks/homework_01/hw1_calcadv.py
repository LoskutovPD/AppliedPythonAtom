#!/usr/bin/env python
# coding: utf-8


def advanced_calculator(input_string):
    if len(input_string) == 0:
        return None
    data_num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 
                '0', '.', '+', '-', '*', '/', '(', ')', ' ', '\t']
    for x in input_string:
        if x not in data_num:
            return None
    if input_string[0] == '-' or input_string[0] == '+':
        input_string = "0" + input_string
    temp = input_string.replace("--", "+")
    while "++" in temp:
        temp = temp.replace("++", "+")
    temp = temp.replace("(", " ( ").replace(")", " ) ")
    temp = temp.replace("+", " + ").replace("-", " - ")
    temp = temp.replace("*", " * ").replace("/", " / ")
    temp = " ".join(temp.split())
    if "* *" in temp or "/ /" in temp or "/ *" in temp \
        or "* /" in temp or "+ *" in temp or "- *" in temp \
        or "+ /" in temp or "- /" in temp or "( )" in temp:
        return None
    try:
        return eval(temp)
    except:
        return None
