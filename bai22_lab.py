# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 18:49:02 2024

@author: DELL _ PC
"""

a= float(input("Nhập số a:"))
b= float(input("Nhập số b:"))
if a != 0:
    x = -b / a
    print("Phương trình có nghiệm duy nhất x =", x)
else:
    if b != 0:
        print("Phương trình vô nghiệm")
    else:
        print("Phương trình có vô số nghiệm")
Biện luận :
    Phương trình có nghiệm duy nhất: x = -b/a
    


