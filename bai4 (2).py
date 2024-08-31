# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 13:22:41 2024

@author: Admin
"""

N = int(input("Nhập số nguyên dương có 2 chữ số: "))
if N > 10 or N < 99:
    a = N//10
    b = N%10
    tong = a+b
    print("Tổng = ",tong)
else:
    print("Số nhập vào không phải số nguyên dương có 2 chữ số.")