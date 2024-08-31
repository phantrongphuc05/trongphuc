
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 13:46:33 2024

@author: Admin
"""
import math 
a = float(input("Nhập hệ số thứ nhất: "))
b = float(input("Nhập hệ số thứ hai: "))
c = float(input("Nhập hệ số thứ ba: "))
delta = b*b-4*a*c 
if a!=0 and delta == 0: 
    x = -b/2*a 
    print("Phương trình có nghiệm kép x1=x2= ",x)
elif a==0:
    z=-b/c 
    print("Phương trình có nghiệm duy nhất x= ",z )
elif a!=0 and delta > 0: 
    x1 = (-b + math.sqrt(delta))/(2*a)
    x2 = (-b - math.sqrt(delta))/(2*a)
    print("x1= ",x1)
    print("x2= ",x2)
elif a!=0 and delta < 0: 
    print("Phương trình vô nghiệm.")
    

    
    
    