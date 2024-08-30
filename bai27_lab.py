# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 11:15:39 2024

@author: DELL _ PC
"""
import math
a = input("Nhập hình (v: hình vuông, n: hình chữ nhật, t: hình tròn): ")

if a == 'v':
    canh = float(input("Nhập chiều dài cạnh của hình vuông: "))
    chu_vi = 4 * canh
    dien_tich = canh * canh
    print("Chu vi =", chu_vi)
    print("Diện tích =", dien_tich)

elif a == 'n':
    rong = float(input("Nhập chiều rộng của hình chữ nhật: "))
    dai = float(input("Nhập chiều dài của hình chữ nhật: "))
    chu_vi = 2 * (rong + dai)
    dien_tich = rong * dai
    print("Chu vi =", chu_vi)
    print("Diện tích =", dien_tich)

elif a == 't':
    ban_kinh = float(input("Nhập bán kính của hình tròn: "))
    chu_vi = 2 * math.pi * ban_kinh
    dien_tich = math.pi * (ban_kinh ** 2)
print("Chu vi =", chu_vi)
print("Diện tích =", dien_tich)

else:
    print("Lựa chọn không hợp lệ. Vui lòng nhập v, n hoặc t.")
