# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 18:56:52 2024

@author: DELL _ PC
"""

so_xe= input(" Nhập xe của bạn( gồm 4 chữ số):")
tong = int(so_xe[0]) + int(so_xe[1]) + int(so_xe[2]) + int(so_xe[3])
sonut = tong % 10
print("Số nút:",sonut)