#!/usr/bin/env python
#encoding:utf-8
__author__ = 'Samren'


def fib1(n):
    def get_num(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return get_num(n-1) + get_num(n-2)
    ret = []
    for x in xrange(n):
        ret.append(get_num(x))
    return ret


def fib2(n):
    """
    当n>2时，直接从默认列表中取最后2个，求和，append到ret中
    """
    if n < 0 or isinstance(n, str):
        raise ValueError("must be number and >=0")
    ret = [0, 1]
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    else:
        for x in xrange(n-2):
            ret.append(ret[-2] + ret[-1])
    return ret


def fib3(n):
    """
    利用math库中的公式生成
    参考链接：http://stackoverflow.com/questions/494594/\
    how-to-write-the-fibonacci-sequence-in-python
    """
    from math import sqrt
    def f(n):
        return int(((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5)))
    ret = []
    for x in xrange(n):
        ret.append(f(x))
    return ret



if __name__ == '__main__':
    n = 10
    print fib1(n)
    print fib2(n)
    print fib3(n)
