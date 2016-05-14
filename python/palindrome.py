#!/usr/bin/env python
#encoding:utf-8
__author__ = 'Samren'

"""
回文数判断：
is_palindrome1 设置2个指针，从头尾逐步移动，
一旦不相等立即返回False，否则成功

is_palindrome2 设置2个指针，从中间向两头逐步移动，
一旦不相等立即返回False，否则成功
"""


def is_palindrome1(s):
    if not isinstance(s, str):
        raise ValueError('Please input a string!')
    front, back = 0, len(s) - 1
    while front < back:
        if s[front] != s[back]:
            return False
        front += 1
        back -= 1
    return True


def is_palindrome2(s):
    if not isinstance(s, str):
        raise ValueError('Please input a string!')
    if len(s) % 2 == 0:
        forward, backward = int((len(s) / 2) - 1), int(len(s) / 2)
    else:
        forward = backward = int(len(s) / 2)
    while backward < len(s):
        if s[forward] != s[backward]:
            return False
        backward += 1
        forward -= 1
    return True


if __name__ == "__main__":
    s1 = 'abba'
    s2 = 'a'
    s3 = 'abcba'
    s4 = 'aacc'
    print(is_palindrome1(s1))
    print(is_palindrome1(s2))
    print(is_palindrome1(s3))
    print(is_palindrome1(s4))
    print(is_palindrome2(s1))
    print(is_palindrome2(s2))
    print(is_palindrome2(s3))
    print(is_palindrome2(s4))
    try:
        print(is_palindrome1(2))
    except ValueError as e:
        print(e)
