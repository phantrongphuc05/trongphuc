# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 19:36:07 2024

@author: Admin
"""

h = int(input("Nhập giờ: "))
p = int(input("Nhập phút: "))
s = int(input("Nhập giây: "))
a = f"{h}h{p}p{s}s"
print("Kết quả:",a)
tổng = h*3600+p*60+s
print("Tổng số giây là:",tổng)