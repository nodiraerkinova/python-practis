a = 4
b = 8
c = 2
arifmetik = (a + b + c) / 3
g = (a * b * c) ** (1 / 3)
print(arifmetik)
print(g)

# String metodlari (methods)
firstname = "John"
lastname = "Doe"
fulname = f"{firstname} {lastname}"
# upper() / lower()
print(fulname.upper())
print(fulname.lower())
print("Adminjon".upper())
# title() / capitalize()
print("Welcom to uzbekiston".title())
print("Where are you from".title())
print("manual tester".capitalize())
fulname = fulname.capitalize() # John doe
print(fulname)

meva = "     olma     "
print("Men " + meva.lstrip() + " yaxshi ko'raman")
print("Men " + meva.rstrip() + " yaxshi ko'raman")
print("Men " + meva.strip() + " yaxshi ko'raman")
print("Men " + meva + " yaxshi ko'raman")

# input()
nickname1 = "rajabboyeva1"
nickname2 = input("Krci, instagramm nickname kirit:")
print("1-account:", nickname1)
print("Foydalanuvchi accounti:", nickname2)

# Amaliyot
kocha = input("Krci, Ko'changizni nomini kirit:")
mahalla = input("Mahallangiz nomi:")
tuman = input("Tumaningizni kiriting:")
viloyat = input("viloyatingizni kiriting:")
print(f"{viloyat} viloyati \n {tuman} tumani \n {mahalla} mahallasi \n {kocha} kocha")

manzil = f"{viloyat} viloyati \n {tuman} tumani \n {mahalla} mahallasi \n {kocha} kocha"
print(manzil.upper())
print(manzil.title())
print(manzil.lower())
print(manzil.capitalize())