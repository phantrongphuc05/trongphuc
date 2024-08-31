# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 15:44:14 2024

@author: Admin
"""

import time 
def time_to_seconds(time_str):
    giờ, phút, giây = map(int, time_str.split(':'))
    tổng_giây = giờ * 3600 + phút * 60 + giây
    return tổng_giây
thời_gian = input("Nhập thời gian theo định dạng hh:mm:ss: ")
số_giây = time_to_seconds(thời_gian)
print("Tổng số giây là: ", số_giây)
