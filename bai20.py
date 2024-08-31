# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 19:52:59 2024

@author: Admin
"""

a = int(input("Nhập số nguyên thứ nhất: "))
b = int(input("Nhập số nguyên thứ hai: "))
c = int(input("Nhập số nguyên thứ ba: "))
số_lớn_nhất = a
if b > số_lớn_nhất:
    số_lớn_nhất = b
if c > số_lớn_nhất:
    số_lớn_nhất = c  
print(f"Số nhỏ nhất là: {số_lớn_nhất}")
