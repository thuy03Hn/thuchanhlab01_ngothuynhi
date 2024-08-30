# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 10:28:54 2024

@author: DELL _ PC
"""

a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
c = float(input("Nhập số c: "))
if a > b:
    a, b = b, a  # Đổi chỗ a và b nếu a > b
if a > c:
    a, c = c, a  # Đổi chỗ a và c nếu a > c
if b > c:
    b, c = c, b  # Đổi chỗ b và c nếu b > c