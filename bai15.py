# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 19:14:08 2024

@author: Admin
"""
import math
a = float(input("Nhập số thứ nhất: "))
b = float(input("Nhập số thứ hai: "))
biểu_thức_1 = (a+b)/((math.pow(a, 1/3))+(math.pow(b, 1/3)))-(math.pow(a*b, 1/3))
biểu_thức_2 = (math.pow(a, 1/3)-math.pow(b, 1/3))**2
phép_tính = (biểu_thức_1)/(biểu_thức_2)
print("Kết quả là",phép_tính)