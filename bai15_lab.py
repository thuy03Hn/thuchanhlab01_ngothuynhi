# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 19:52:03 2024

@author: DELL _ PC
"""
import math
a= float(input("Nhập số a:"))
b= float(input("Nhập số b:"))
cb3a = math.pow(a,1/3)
cb3b = math.pow(b,1/3)
ab = a*b
cb3ab = math.pow(ab,1/3)
tuso = ( ( a+b)/(cb3a + cb3b)) - cb3ab
mauso = ( cb3a - cb3b)**2
A = (tuso)/(mauso)
print(" Kết quả:", A)


