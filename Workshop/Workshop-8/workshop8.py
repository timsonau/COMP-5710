'''
Author: Akond Rahman
Code needed for Workshop 8
'''

from ast import operator
import random


def divide(v1, v2):
    temp = 0
    if (isinstance(v1, int) and isinstance(v2, int)):
        if v2 > 0:
            temp = v1/v2
        elif v2 < 0:
            temp = v1/v2
        else:
            temp = "Divisior is zero. provide non-zero values."
    else:
        temp = 'please provide numeric values'
    return temp


def fuzzValues():
    # positive or expected software testing
    res = divide(2, 1)
    print(res)
    print('='*100)
    # negative software testing: > 0 divisior test
    res = divide(2, 0)
    print(res)
    print('='*100)
    # negative software testing: > 0 divisior test
    res = divide(2, -1)
    print(res)
    print('='*100)
    # negative software testing:  non string divisior
    res = divide(2, '1')
    print(res)
    print('='*100)


def simpleFuzzer():
    fuzzValues()


if __name__ == '__main__':
    simpleFuzzer()
