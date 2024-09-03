# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 15:35:07 2024

@author: Admin
"""

a = int(input("Nhập số xe gồm 4 số: "))
số_đầu = a // 1000
số_thứ_hai = ((a % 1000) // 100)
số_thứ_ba = ((a % 1000) % 100) // 10
số_cuối = (a % 10)
biển_số_xe = (số_đầu,số_thứ_hai,số_thứ_ba,số_cuối)
số_nút = sum(biển_số_xe)
if 0 <= số_nút <= 9:
    print(f"Số nút của bạn là {số_nút} nút")
else:
    a = số_nút // 10
    b = số_nút % 10
    số_mới = a + b
    c = số_mới // 10
    d = số_mới % 10
    print("Số nút mới là: ", c + d)
    
