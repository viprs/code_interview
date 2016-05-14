#!/usr/bin/env python
#encoding:utf-8
__author__ = 'Samren'
"""
算法：快速排序
对无序的列表进行快速排序，使用递归的方法，关键在于"划分"(partition)
"""


def partition(lst, low, high):
    if len(lst) < 1:
        return -1
    pivotloc = lst[low]
    while low < high:
        while low < high and lst[high] >= pivotloc:
            high -= 1
        lst[low] = lst[high]
        while low < high and lst[low] <= pivotloc:
            low += 1
        lst[high] = lst[low]
    lst[low] = pivotloc
    return low


def q_sort(lst, low, high):
    if low < high:
        pivotloc = partition(lst, low, high)
        q_sort(lst, low, pivotloc-1)
        q_sort(lst, pivotloc+1, high)


def quick_sort(lst):
    q_sort(lst, 0, len(lst)-1)


if __name__ == '__main__':
    lst = [8, 10, 9, 6, 4, 16, 5, 13, 1]
    quick_sort(lst)
    print lst
    #assert(lst == [1, 4, 5, 6, 8, 9, 10, 13, 16], "quick sort error")