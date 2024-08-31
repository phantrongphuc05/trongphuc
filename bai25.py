# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 20:30:29 2024

@author: Admin
"""

chữ_thường = input("Nhập kí tự chữ thường: ")
chữ_hoa = input("Nhập kí tự viết hoa: ")
in_hoa = chữ_thường.upper()
viết_thường = chữ_hoa.swapcase()
print("Kí tự viết hoa là:",in_hoa)
print("Kí tự viết thường là:",viết_thường)