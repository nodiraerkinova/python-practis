# Ma'lumot turlari (Dats types)
# 1. String(matn) 
# 2. Number(son) => 1. Integer(butun son) 5 -5 10 ; 2. Float(O'nlik son) 5.75 -8.99 0.75
# 3. Boolean(Mantiqyi qiymat) => 1. True 2. False
text = "lorem ipsum"
age = 28
is_student = True
# type() - type checking
print(type(text)) # str
print(type(-78)) #int
print(type(8.97)) #float
print(type(is_student)) #bool 

# a = 20
# b = -30
# c = a + b
# print(c) # 10 

pi = 3.1415
radius = 10
d = 2 * radius
yuza = pi * radius ** 2
print(d)
print(yuza) 

# a = 2
# b = 3.0
# # Quyidagi arifmetik amallarning natijasi o'nlik son hosil qiladi
# print(a+b) 
# print(a*b)
# print(a**b)
# print(2*(a+b)) 

aholi_soni = 7_594_000_000 # o'zmizga qulay bo'lishi uchun shinday yozdik
print("Yer kurrasida", aholi_soni, " ga yaqin odam yashaydi")

PI = 3.1415
G = 9.81
print(PI, G)

# # x = 7
# # y = -5
# # z = 10
# x, y, z = 7, -5, 10
# print(x + y - z)

kv_tomoni = int(input("Kvadrat tomonini kiriting")) #5 => "5"; True => "True") 
print(kv_tomoni ** 2)

ism = "Jobir"
yosh = 36
xabar = ism + " " + str(yosh) +  " yoshda"
print(xabar)
print(int(5.36)) # 5 
print(float('8.87'))

# Amaliyot
t_yil = int(input("Tug'ilgan yilingizni kiriting: "))
yosh = 2025 - t_yil
print(yosh) 

x = int(input("Istalgan son kiriting:"))
# print(x, " ning kvadrati ", x**2, " ga teng")
# print(x, " ning kubi ", x**3, " ga teng")
xabar1 = str(x) + "ning kvadrati" + str(x ** 2) + "ga teng"
xabar2= str(x) + "ning kubi" + str(x ** 3) + "ga teng"
print(xabar1)
print(xabar2)

yosh = int(input("Yoshingiz nechida? "))
t1_yil = 2025-yosh
print("Siz ", t1_yil, " da tug'ilgansiz")

a = float(input("Birinchi sonni kiriting: "))
b = float(input("Ikkinchi sonni kiriting: "))
print(f"a + b =", a + b)
print(f"a - b =", a - b)
print(f"a * b =", a * b)
print(f"a / b =", a / b) 