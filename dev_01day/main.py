#!/usr/bin/python3
# -*-coding:utf8-*-
# @Author:Administrator
# @Time:2022/12/30 21:48
from book import Book, BookManage

def welcome():
    print("******************欢迎进入图书管理系统**************")
    print("1.显示所有图书\n2.添加图书\n3.删除图书\n4.查找图书\n5.退出\n6.清空数据|\n7.保存")
    print("************************************************")

def get_choose_number():
    """获得用户输入输入的菜单编号"""
    choose_number = input("请输入菜单编号：")
    # 如果编号不是数字或者不是不是12345返回-1
    if not choose_number.isdigit() or choose_number not in ['1','2','3','4','5','6','7']:
        return -1
    return choose_number

def main():
    bm = BookManage()   # 创建一个用来管理图书的对象
    while True:
        welcome()
        number = get_choose_number()
        if number == -1:
            print("编号输入有误，请重新输入！")
            continue

        if number == "1":
            bm.show_book()

        elif number == "2":
            book_name = input("请输入书名：")
            book_position = input("请输入位置：")
            # 创建一个对象，具体的书
            book = Book(bm.last_book_id + 1, book_name, book_position)
            bm.add_book(book)
            # book = Book
        elif number == "3":
            pass

        elif number == "4":
            pass

        elif number == "5":
            pass

        elif number == "6":
            bm.clean()

        elif number == "7":
            bm.save()

        else:
            break

if __name__ == '__main__':
    main()