#!/usr/bin/python3
# -*-coding:utf8-*-
# @Author:Administrator
# @Time:2022/12/30 22:07
import os
import pickle

class Book(object):
    def __init__(self, num, name, position):
        self.num = num
        self.name = name
        self.position = position

    def __str__(self):
        """
        自定义print对象时显示的格式
        :return:
        """
        return f"{self.num}\t{self.name}\t{self.position}"

class BookManage(object):
    book_list = []

    def __init__(self):
        # 构造方法__init__
        # __init__方法在对象被初始化的时候，自动执行
        print("__init__ is running...")

        # 加载文件到内存

        # 避免异常有两种方法：一、加判断；二、异常处理
        if not os.path.isfile("book.data"):
            pickle.dump(self.book_list, open("book.data", "wb"))    # 把对象保存到文件

        # 确保每次运行程序前，先把book.data文件中所有内存load到book_list中
        self.book_list = pickle.load(open("book.data", "rb"))    # 把文件中的内容加载到内存

    def show_book(self):
        """显示所有图书"""
        for book in self.book_list:
            print(book)

    def add_book(self, book:Book):
        self.book_list.append(book)

    def del_book_by_name(self,name:str):
        pass

    def clean(self):
        self.book_list = []

    @property
    def last_book_id(self):
        """如果book_list是空，返回0，否则
        返回最后一本书的num值"""
        if self.book_list:
            last_book = self.book_list[-1]    # 获得list中最后一本书
            return last_book.num
        return ()

    def __del__(self):
        """把内存中的数据保存到文件"""
        # 析构方法
        # __del__在对象被销毁的时候自动执行
        print("__del__ is running...")
        # dump  把对象保存到 磁盘
        # 确保 退出时 把所有对book_list的变更持久化到book.data文件中
        pickle.dump(self.book_list, open("book_data","wb"))  # 把对象保存到文件

    def save(self):
        """把内存中的数据保存到文件"""
        pickle.dump(self.book_list,open("book_data","wb"))    # 把对象保存到文件






