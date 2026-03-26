# Function - ma'lum vazifani bajaruvchi kod bloki.
# Funksiya yaratish uchun def kalit so'zidan foydalanamiz
# Pythndagi tayyor funksiyalar - print(), input(), len()
print("Hello world")
# Funksiya ne'lon qilish(declaration)
# def salom_ber():
#     print("Salom dunyo")

# # Funksiyani chaqirish(call)
# salom_ber() #Natija: Salom dunyo

# Funksiya parametrlar, argumentlar
def salom_ber(ism):
    print(f"Assalomu aleykum, {ism}!")

salom_ber("Asadbek")
salom_ber("Ali")
salom_ber("Vali")

def yigindi(a, b):
    print(a + b)

yigindi(7, 8)
yigindi(10, 20)

def calculate_age(birth_year, name):
    age = 2026 - birth_year
    print(f"{name}ning yoshi {age}")

calculate_age(1990, "Ali")
calculate_age(1985, "Vali")
calculate_age()