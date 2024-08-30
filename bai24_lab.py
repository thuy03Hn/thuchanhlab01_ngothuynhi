# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 19:27:28 2024

@author: DELL _ PC
"""

a = int(input("Nhập giờ:"))
b = int(input("Nhập phút:"))
c = int(input("Nhập giây:"))
if 0 < a <= 24 and 0<= b <60 and 0<= c<60: 
    print(" Giờ, phút giây hợp lệ:")
else:
    print("Giờ, phút, giây không hợp lệ:")
    