#!/usr/bin/python3
# -*-coding:utf8-*-
# @Author:Administrator
# @Time:2022/12/31 10:47


for i in [1,2,3]:
    print(i)

print(hasattr(list,"__iter__"))
print(hasattr(tuple,"__iter__"))
print(hasattr(set,"__iter__"))
print(hasattr(str,"__iter__"))
print(hasattr(dict,"__iter__"))
print(hasattr(int,"__iter__"))

# for i in 1:
#     print(i)