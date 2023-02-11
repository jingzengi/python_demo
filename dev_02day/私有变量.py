#!/usr/bin/python3
# -*-coding:utf8-*-
# @Author:Administrator
# @Time:2022/12/31 10:30


def test_private_vs_protected_vs_public():
    # public:共有的
    # protected:受保护的.不能被其他文件导入
    # private ：私有的
    pass
x = 2
_y = 10

class A(object):
    def __init__(self):
        self.__z = 2

    def __some_method(self):
        print(self)

a = A()

if __name__ == '__main__':
    test_private_vs_protected_vs_public()