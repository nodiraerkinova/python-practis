# Returne function
# def sum_list(lst):
#     s = 0
#     for element in lst:
#         s += element

#     return s    

# print(sum_list([1, 2, 3, 4, 5]))

# Flexible(muslashuvchan) function
# *args usuli 
# def summa(*numbers):
#     # print(numbers) (a, b, c, d, ...)
#     # print(type(numbers)) (tuple)
#     s = 0
#     for number in numbers:
#         s += number
#     return s

# print(summa(12, 50, 89, -89, 0, -77))


# def my_func(*people):
#     print(f"The youngest person is {people[1]}")

# my_func("Ali", "Vali", "Guli", "Soli")
# my_func("Oysara", "Tojivoy", "Qo'zivoy", "Gulbaxor")

# def summa(x, y, *sonlar):
#     return x + y + sum(sonlar)

# print(summa(1, 7, 8, 9, 10))

# **kwargs(keyword arguments) usuli
# def avto_info(kompaniya, model, **malumotlar):
#     # print(malumotlar)
#     # print(type(malumotlar))
#     malumotlar['kompaniya'] = kompaniya
#     malumotlar['model'] = model

#     return malumotlar


# print(avto_info("GM", "Malibu", rang="qora", yil=2020, narh=35000))
# print(avto_info("Toyota", "Camry", rang="oq", yil=2021, narh=40000, korobka="avtomat"))

# def my_func(**kid):
#     print("His last name is " + kid["last_name"])

# my_func(fname= "Tobias", lname= "Funk")

# Amaliyot
# 1
def kopaytma(*numbers):
    s = 1
    for number in numbers:
        s *= number
    return s
print(kopaytma(1, 2, 3, 4, 5)) 

# 2
def t_haqida(ism, familiya, **qoshimcha_malumotlar):
    talaba = {
        "ism": ism,
        "familiya": familiya
    }
    
    talaba.update(qoshimcha_malumotlar)
    
    return talaba

talaba1 = t_haqida("Lobar", "Ramatova", yosh = 20)

print(talaba1)
