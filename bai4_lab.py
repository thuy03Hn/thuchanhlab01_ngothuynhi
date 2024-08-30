# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 18:23:42 2024

@author: DELL _ PC
"""
N = int(input("Nhập số nguyên dương có 2 chữ số:"))
if 10 <= N <= 90:
    donvi = N %10
    chuc = N // 10
    Tong = chuc +  donvi
    print(" Tổng hai chữ số N:", Tong)
    