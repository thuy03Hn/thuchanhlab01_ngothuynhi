# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 18:26:47 2024

@author: DELL _ PC
"""

a =input(" Nhập giờ, phút, giây theo định dạng(hh:mm:ss):")
b = a.split(":")
gio = int(b[0])
phut = int(b[1])
giay = int(b[2])
sogiay = gio*3600 + phut*60 + giay
print("Tổng số giây là:",sogiay)