# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 15:57:48 2024

@author: Admin
"""
#Giờ 1
hour1 = int(input("Nhập số giờ thứ 1: "))
minutes1 = int(input("Nhập số phút thứ 1: "))
seconds1 = int(input("Nhập số giây thứ 1: "))
a = f"{hour1}h {minutes1}p {seconds1}s"
print("Thời gian thứ nhất: ", a)
#Giờ 2
hour2 = int(input("Nhập số giờ thứ 2: "))
minutes2 = int(input("Nhập số phút thứ 2: "))
seconds2 = int(input("Nhập số giây thứ 2: "))
b = f"{hour2}g, {minutes2}p, {seconds2}s"
print("Thời gian thứ hai: ", b)
#Tổng
tổng_giờ = hour1 + hour2
tổng_phút = minutes1 + minutes2
tổng_giây = seconds1 + seconds2
tổng_thời_gian = f"{tổng_giờ}h, {tổng_phút}p, {tổng_giây}s"
print("Tổng 2 thời gian là: ", tổng_thời_gian)
#Hiệu 
#Giờ 1 - giờ 2 
hiệu_giờ1 = hour1 - hour2
hiệu_phút1 = minutes1 - minutes2
hiệu_giây1 = seconds1 - seconds2
hiệu_thời_gian1 = f"{hiệu_giờ1}h, {hiệu_phút1}p, {hiệu_giây1}s"
#Giờ 2 - giờ 1 
hiệu_giờ2 = hour2 - hour1
hiệu_phút2 = minutes2 - minutes1
hiệu_giây2 = seconds2 - seconds1
hiệu_thời_gian2 = f"{hiệu_giờ2}h, {hiệu_phút2}p, {hiệu_giây2}s"
if hour1 > hour2 and minutes1 > minutes2 and seconds1 > seconds2:
     print("Hiệu 2 thời gian là: ", hiệu_thời_gian1)
elif hour2 > hour1 and minutes2 > minutes1 and seconds2 > seconds1:
     print("Hiệu 2 thời gian là: ", hiệu_thời_gian2)
else:
     print(" Thời gian không hợp lệ")
