# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 19:05:17 2024

@author: DELL _ PC
"""
a= float(input("Nhập số a:"))
b= float(input("Nhập số b:"))
c= float(input("Nhập số c:"))
delta = b**2 - 4*a*c 
if delta >0:
 x1 = (-b + math.sqrt(delta))/(2*a)
 x2 = (-b- math.sqrt(delta))/(2*a)
 print("Phương trình có hai nghiệm:")
 print("x1=", x1)
 print("x2=",x2)
elif delta==0:
    x = -b/2*a
    print("Phương trình có nghiệm kép:",x)
else:
    print("Phương trình vô nghiệm:")
    Biện luận :
    delta = b**2 - 4*a*c
Nếu delta > 0: Phương trình có 2 nghiệm phân biệt.
Nếu delta = 0: Phương trình có 1 nghiệm kép.
Nếu delta < 0: Phương trình vô nghiệm 
 delta >0:
 x1 = (-b + math.sqrt(delta))/(2*a)
 x2 = (-b- math.sqrt(delta))/(2*a)
 Phương trình có hai nghiệm:
 delta==0:
     x = -b/2*a
     Phương trình có nghiệm kép:
 delta < 0 : Phương tình vô nghiệm        