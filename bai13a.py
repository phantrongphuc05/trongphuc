# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 16:33:39 2024

@author: Admin
"""

ngay = input("Nhập ngày sinh : ")
thang = input("Nhập tháng sinh : ")
nam = input("Nhập năm sinh : ")
ngay = ngay.zfill(2)
thang = thang.zfill(1)
nam = nam.zfill(4)
print(f"{ngay}/{thang}/{nam}")
#ngược lại 
ngay = input("Nhập ngày sinh : ")
thang = input("Nhập tháng sinh : ")
nam = input("Nhập năm sinh : ")
ngay = ngay.zfill(2)
thang = thang.zfill(1)
nam = nam.zfill(4)
print(f"{nam}/{thang}/{ngay}")
