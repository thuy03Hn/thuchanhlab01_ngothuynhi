# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 22:30:21 2024

@author: DELL _ PC
"""

# Nhập thời gian thứ nhất
gio1 = int(input("Nhập giờ thứ nhất: "))
phut1 = int(input("Nhập phút thứ nhất: "))
giay1 = int(input("Nhập giây thứ nhất: "))

# Nhập thời gian thứ hai
gio2 = int(input("Nhập giờ thứ hai: "))
phut2 = int(input("Nhập phút thứ hai: "))
giay2 = int(input("Nhập giây thứ hai: "))

# Cộng hai giờ
tong_giay = giay1 + giay2
tong_phut = phut1 + phut2
tong_gio = gio1 + gio2

if tong_giay >= 60:
    tong_giay = tong_giay - 60
    tong_phut = tong_phut + 1

if tong_phut >= 60:
    tong_phut = tong_phut - 60
    tong_gio = tong_gio + 1

print("Tổng thời gian là:", tong_gio, "giờ", tong_phut, "phút", tong_giay, "giây")

# Trừ hai giơf 
hieu_giay = giay1 - giay2
hieu_phut = phut1 - phut2
hieu_gio = gio1 - gio2
if hieu_giay < 0:
    hieu_giay = hieu_giay + 60
    hieu_phut = hieu_phut - 1
if hieu_phut < 0:
    hieu_phut = hieu_phut + 60
    hieu_gio = hieu_gio - 1

print("Hiệu thời gian là:", hieu_gio, "giờ", hieu_phut, "phút", hieu_giay, "giây")