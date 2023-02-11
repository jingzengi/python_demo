#!/usr/bin/python3
# -*-coding:utf8-*-
# @Author:Administrator
# @Time:2023/2/9 8:37

user = "user1"
passwd = "123456"
count = 0
for i in range(3):
    username = input("请输入用户名：")
    password = input("请输入密码：")
    if username == user and password == passwd:
        print("登陆成功")
        count = 3
        break
    else:
        print("账户或密码错误")
        count +=1
        print("剩余",2-i,"次机会")


