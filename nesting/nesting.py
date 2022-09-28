# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 11:06:20 2022
#Lesson - Nesting
@author: Idris
"""
# =============================================================================
# 
# car0 = {
#         "model":"lacetti",
#         "rang":"oq",
#         "yil":2018,
#         "narx":1300,
#         "km":50000,
#         "korobka":"avtomat"
#         }
# car1 = {
#         "model":"nexia 3",
#         "rang":"qora",
#         "yil":2015,
#         "narx":9800,
#         "km":89000,
#         "korobka":"mexanika"
#         }
# car2 = {
#         "model":"gentra",
#         "rang":"qizil",
#         "yil":2019,
#         "narx":1500,
#         "km":20000,
#         "korobka":"mexanika"
#         }
# cars = [car0, car1, car2]
# =============================================================================
# =============================================================================
# for car in cars:
#     print(f"{car['model'].title()} "
#       f"rangi:{car['rang']} "
#       f"yili:{car['yil']} "
#       f"narxi:{car['narx']}$")
# =============================================================================
    
# =============================================================================
# print(f"Moshina:{cars[1]['model']}, Rangi:{cars[1]['rang']}")  
# =============================================================================
    
malibus = []
for n in range(10):
    new_car = {
        "model":"malibu",
        "rang":None,
        "yil":2015,
        "narx":None,
        "km":0,
        "korobka":"mexanika"
        }
    malibus.append(new_car)
    
for malibu in malibus[0:3]:
    malibu['rang']=['oq']
# =============================================================================
#     print(malibus)
# =============================================================================

for malibu in malibus[3:6]:
    malibu['rang']=['qizil']
# =============================================================================
#     print(malibus)    
# =============================================================================
for malibu in malibus[6:]:
     malibu['rang']=['qora']
     malibu['korobka']=['avto']
     print(malibus)   
    
for malibu in malibus:    
    if malibu['korobka']==['avto']:
       malibu['narx']=4000
    else:
       malibu['narx']=3000

print(malibus)      