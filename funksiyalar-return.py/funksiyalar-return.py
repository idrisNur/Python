# def toliq_ism_yasa(familiya, ism, otasining_ismi=""):
#     """To`liq ism qaytaruvchi funksiya"""
#     if otasining_ismi:
#         toliq_ism_yasa= f"{familiya} {ism} {otasining_ismi}"
#     else:
#         toliq_ism_yasa= f"{familiya} {ism}"
#     return toliq_ism_yasa.title()

# talaba = toliq_ism_yasa("musulmonov", "idris", "nurmuhammad")
# talaba_2 = toliq_ism_yasa("musulmonov", "quddus")
# print(talaba, "va", talaba_2)

""" def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
    avto={
        "kompaniya": kompaniya,
        "model": model,
        "rangi": rangi,
        "korobka": korobka,
        "yili": yili,
        "narhi": narhi, 
    }
    return avto
avto_1 = avto_info("GM", "Nexia", "Oq", "Avtomat", "2022")
avto_2 = avto_info("GM", "Nexia2", "Qora", "Mexanik", "2021", 5500) """

""" avtolar = [avto_1, avto_2]
print("Onlayn bozordagi avtomashinalar:")
for avto in avtolar:
    if avto['narhi']:
        narh = avto["narhi"]
    else:
        narh = "Noma'lum"
    print(f"{avto['rangi']} {avto['model']}. Narhi: {avto['narhi']}.") """

""" sonlar = list(range(1,11))
print(sonlar) """

""" def oraliq(min, max, qadam=1):
    sonlar=[]
    while min<max:            
        sonlar.append(min)
        min+=qadam
    return sonlar

print(f"Juft sonlar: {oraliq(2,21,2)}") """
