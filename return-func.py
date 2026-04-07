# # def is_even(number):
# #     if number % 2 == 0:
# #         return "Juft"
# #     else:
# #         return "False"
    
# # print(is_even(4)) # juft
# # result = is_even(7)
# # print(result)

# # Ternary operator yordamida yuqoridagi funksiyani qisqartirish mumkin:
# # syntax: value_if_true if condition else value_if_fal

# def is_even(number):
#     return "juft" if number % 2 == 0 else "toq"

# print(is_even(4)) # juft
# print(is_even(7)) # toq

# volwes = ["a", "o", "i", "u", "e"]
# def count_volwes(text):
#     count = 0
#     for char in text:
#         if char in volwes:
#             count += 1 
#     return count

# print(count_volwes("javascript"))
# print(count_volwes("python"))

# # string bo'yicha for loop ishlatish
# # text = "Hello world"
# # for char in text:
# #     print(char)

# def toliq_ism_yasa(ism, familiya, otasining_ismi=''):
#     """Toliq isma qaytaruvchi funksiya"""
#     if otasining_ismi: # otasining_ismi mavjudligini tekshiramiz
#         toliq_ism = f"{ism} {otasining_ismi} {familiya}"
#     else:
#         toliq_ism = f"{ism} {familiya}"
#     return toliq_ism.title() 

# talaba1 = toliq_ism_yasa('olim','hakimov') #otasining_ismi kiritilmadi
# talaba2 = toliq_ism_yasa('hakim','olimov','abrorovich')
# print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")

# def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
#     avto = {'kompaniya':kompaniya,
#             'model':model,
#             'rang':rangi,
#             'korobka':korobka,
#             'yil':yili,
#             'narh':narhi}
#     return avto

# avto1 = avto_info('GM', 'Malibu', 'Qora', 'Avtomat', 2020)
# print(avto1)        
