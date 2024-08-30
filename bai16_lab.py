# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 18:10:55 2024

@author: DELL _ PC
"""
a1 = input("Nhập giờ/phút/giây:")
a2 = a1.split("/")
a = int(a2[0])
b = int(a2[1])
c = int(a2[2])
sogiay = a*3600 + b*60 +c
print("Tổng số giây:",sogiay)
