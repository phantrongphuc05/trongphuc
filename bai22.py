# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 13:34:42 2024

@author: Admin
"""

a = float(input("Nhập hệ số thứ nhất: "))
b = float(input("Nhập hệ số thứ hai: "))
if a==0 and b==0:
    print("Phương trình vô số nghiệm.")
elif a==0 and b!=0:
    print("Phương trình vô nghiệm.")
elif a!=0 and b==0:
    print("Phương trình vô nghiệm.")
else: 
    x = -b/a
    print("Phương trình có nghiệm x= ",x)