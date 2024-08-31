# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 15:35:07 2024

@author: Admin
"""

import random 
a = random.randrange(0, 9)
b = random.randrange(0, 9)
c = random.randrange(0, 9)
d = random.randrange(0, 9)
tổng = a+b+c+d 
if 0<=tổng<=36:
    print("Số xe của bạn được",tổng,"nút")
else: 
    print("Số xe không hợp lệ.")
    
