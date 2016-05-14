#!/usr/bin/env python
#encoding:utf-8
__author__ = 'Samren'
"""
二分查找算法实现：对已排序的list进行二分查找
binary_search(lst, n): 查找成功，返回位置，失败，返回-1
input:
lst 要查找的list
n 要查找的数
"""


def binary_search(lst, n):
    if len(lst) == 0:
        return -1
    low, high = 0, len(lst) - 1
    while low <= high:
        mid = (low + high) / 2
        if lst[mid] > n:
            high = mid - 1
        elif lst[mid] < n:
            low = mid + 1
        else:
            return mid
    return -1


if __name__ == '__main__':
    a = [1, 3, 5, 7, 9, 11]
    assert(binary_search(a, 3) == 1)
    assert(binary_search(a, 7) == 3)
    assert(binary_search(a, 4) == -1)