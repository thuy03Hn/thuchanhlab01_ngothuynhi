# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 18:35:11 2024

@author: DELL _ PC
"""
a= int(input("Nhập một số bất kì từ 0 đến 9:"))
if 0<= a <=9:
 chuso = { 0:"Không",
         1:"Một",
         2:"Hai",
         3:"Ba",
         4:"Bốn",
         5:"Năm",
         6:"Sáu",
         7:"Bảy",
         8:"Tám",
         9:"Chín"}
 print("Giá trị chuổi của số nguyên:",chuso[a])
else:
    print("Không đọc được:")
    
