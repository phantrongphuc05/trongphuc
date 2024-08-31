# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 20:56:11 2024

@author: Admin
"""

N = input("Nhập số nguyên N: ")
a = list(N)
a.sort()
b = ''.join(a)
print("Số theo thứ tự tăng dần là:", b)
