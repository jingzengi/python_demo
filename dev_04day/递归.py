#!/usr/bin/python3
# -*-coding:utf8-*-
# @Author:Administrator
# @Time:2023/1/1 15:00

import os

def print_all_files(file_path):
    for root, dirs, files in  os.walk(file_path):
        for filename in files:
            print(os.path.join(root,filename))


def print_all_files2(file_path):
    """
    获得file_path下所有文件及文件夹
    如果是文件，直接输出
    如果是文件夹，递归调用
    :param file_path:
    :return:
    """

    for item in os.scandir(file_path):
        if item.is_file():
            print(item.path)
        elif item.is_dir():
            print_all_files2(item.path)

def recode(n):
    print(f"这是第{n}层")
    if n == 1:
        return None
    else:
        n -= 1
        recode(n)

if __name__ == '__main__':
    p = "D:/Python/Python39"
    print_all_files(p)
    recode(20)