# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 22:08:46 2024

@author: DELL _ PC
"""

a = int(input("Nhập số thứ 1:"))
b = int(input("Nhập số thứ 2:"))
c = int(input("Nhập số thứ 3:"))

lonnhat = a

if b > lonnhat:
    lonnhat = b
if c > lonnhat:
    lonnhat = c
print("Giá trị lớn nhất:", lonnhat)

nhoNhat = a

if b < nhoNhat:
    nhoNhat = b
if c < nhoNhat:
    nhoNhat = c
print("Giá trị nhỏ nhất:", nhoNhat)
