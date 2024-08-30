# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 18:21:37 2024

@author: DELL _ PC
"""

a= int(input("Nhập số nguyên thứ 1:"))
b= int(input(" Nhập số nguyên thứ 2:"))
c= int(input("Nhập số nguyên thứ 3:"))
d= int(input("Nhập số nguyên thứ 4:"))
nhonhat = a
if b < nhonhat:
    nhonhat = b
if c < nhonhat:
    nhonhat = c
if d < nhonhat:
    nhonhat = d
print(" Giá trị nhỏ nhất:",nhonhat)
    