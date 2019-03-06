#!/usr/bin/env python
# coding: utf-8


def is_bracket_correct(input_string):
    if len(input_string) == 0:
        return True
    while len(input_string) > 0:
        x1 = input_string.find("()")
        x2 = input_string.find("{}")
        x3 = input_string.find("[]")
        if x1 + x2 + x3 == -3:
            return False
        if x1 != -1:
            input_string = input_string[:x1] + input_string[x1+2:]
        if x2 != -1:
            input_string = input_string[:x2] + input_string[x2+2:]
        if x3 != -1:
            input_string = input_string[:x3] + input_string[x3+2:]
    return True