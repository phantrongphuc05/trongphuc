# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 19:45:24 2024

@author: Admin
"""

a = int(input("Nhập số nguyên thứ nhất: "))
b = int(input("Nhập số nguyên thứ hai: "))
c = int(input("Nhập số nguyên thứ ba: "))
d = int(input("Nhập số nguyên thứ tư: "))
số_nhỏ_nhất = a
if b < số_nhỏ_nhất:
    số_nhỏ_nhất = b
if c < số_nhỏ_nhất:
    số_nhỏ_nhất = c
if d < số_nhỏ_nhất:
    số_nhỏ_nhất = d  
print(f"Số nhỏ nhất là: {số_nhỏ_nhất}")
