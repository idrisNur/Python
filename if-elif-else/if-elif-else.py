# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 14:54:59 2022

@author: User
"""

# =============================================================================
# yosh = int(input("Yoshingiz nechida?\n>>"))
# vazn = int(input("Vazningiz necha kilo?\n>>"))
# if yosh<=5 and vazn<=40:
#     narx=0
# elif yosh<=14 and vazn<=50:
#     narx=5000
# elif yosh<=18 and vazn<=55:
#     narx=8000
# elif yosh<=55 and vazn<=60:
#     narx=10000
#     
# print(f"Sizga minish narxi {narx} so`m.")
# =============================================================================

# =============================================================================
# kun = input("Bugun nima kun?>>>")
# pul = input("Pul bormi?>>>")
# 
# if kun.lower()=="bozor"and pul.lower()=="bor":
#     print("Bozorga ketdikmi unda!\n")
# else:
#     print("Unda ishlarni qilamiz.\n")
# =============================================================================

# =============================================================================
# menu = ['osh','manti','shashlik','mastava','somsa']
# =============================================================================
# =============================================================================
# buyurtma = input("Nima buyurtma qilasiz?\n Taom nomini kiriting:")
# miqdori = float(input("Nechta buyurtma berasiz?"))
# 
# if buyurtma.lower() in menu:
#     print(f"{miqdori}","Buyurtmangiz qabul qilindi, tez orada yetkazamiz!")
# else:
#     print("Afsuski bizda bunday taom yo`q edi!")
# =============================================================================
menu = ['osh','manti','shashlik','mastava','somsa']
buyurtmalar = [input("Quyuq taomdan buyurtma bering:"),input("Suyuq taomdan buyurtma bering:") ]
if buyurtmalar:
    for taom in buyurtmalar:
     if taom in menu:
         print(f"\n Menuda {taom} bor.")
     else:
         print(f"\n Kechirasiz, {taom} tugagan edi!")






























