# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 10:31:09 2024

@author: DELL _ PC
"""

a = int(input("Nhập số nguyên a:"))
b = int(input("Nhập số nguyên b:"))
c = int(input("Nhập số nguyên c:"))
d = int(input("Nhập số nguyên d:"))
#số nhỏ thứ 1
nhonhat = a
if b < nhonhat:
    nhonhat = b
if c < nhonhat:
    nhonhat = c
if d< nhonhat:
    nhonhat = d
# số nhỏ thứ 2
if nhonhat==a:
    nho2 = b
else:
    nho2 = a
if b > nhonhat and b < nho2:
    nho2 = b
if c > nhonhat and c < nho2:
    nho2 = c
if d > nhonhat and d < nho2:
    nho2 = d
#số nhỏ thứ 3
if nho2 == a or nhonhat == a:
    nho3 = b
else:
    nho3 = a

if b > nho2 and b > nhonhat and b < nho3:
    nho3 = b
if c > nho2 and c > nhonhat and c < nho3:
    nh3 = c
if d > nho2 and d > nhonhat and d < nho3:
    nho3 = d

# số cuối cùng là lớn nhất
if nhonhat != a and nho2 != a and nho3 != a:
    lonnhat = a
elif nhonhat != b and nho2 != b and nho3 != b:
    lonnhat = b
elif nhonhat != c and nho2 != c and nho3 != c:
    lonnhat = c
else:
    lonnhat = d
# In kết quả
print("Số theo thứ tự tăng dần:", nhonhat, nho2, nho3, lonnhat)