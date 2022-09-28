# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 14:43:09 2022

@author: Idris: lesson for dictionary.2
"""

# =============================================================================
# talaba_0 = {'ism':'murod olimov','yosh':20,'t_yil':2000}
# print(f"{talaba_0['ism'].title()},\
#  {talaba_0['t_yil']}-yilda tu'gilgan,\
#  {talaba_0['yosh']} yoshda")
# =============================================================================
# =============================================================================
# talaba_1 = {"ism":"Idris Musulmonov", "yosh":27, "yil":"2022"}
# # =============================================================================
# # print(f"{talaba_1['ism']}, {talaba_1['yosh']}yoshda, {talaba_1['yil']}-yilda tug`ilgan.")
# # =============================================================================
# print(talaba_1['ism'])
# =============================================================================
# =============================================================================
# talaba = {"ism":"idris","yosh":27,"yil":1995,"kurs":1}
# for key, value in talaba.items():
#     print(f"{key.title()} {value} \n")
# =============================================================================

# =============================================================================
# telefon = {
#         "ali":"iphone X",
#         "vali":"samsung S10",
#         "olim":"galaxy A30"
#         }
# for key, value in telefon.items():
#     print(f"{key.title()}ning telefoni {value.title()}")
# =============================================================================


mahsulotlar = {
        "olma":15000,
        "anor":12000,
        "banan":18000,
        "uzum":5000,
        "nok":16000,
        "snickers":9000
        }
# =============================================================================
# print("Do'kondagi mahsulotlar:")
# for mahsulot in mahsulotlar.keys():
#     print(mahsulot.title())
# =============================================================================

 
bozorlik = {"non","uzum","go'sht","banan","snickers"}
for mahsulot in mahsulotlar:
     if mahsulot in bozorlik:
         print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")

for buyum in bozorlik:
    if buyum not in mahsulotlar:
        print(f"Iltimos do'koningizga {buyum.title()} ham olib keling!")
























