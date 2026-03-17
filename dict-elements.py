# Dictionary elementlari bilan ishlash
phone = {
    'brand': 'Apple',
    'model': 'iPhone 17 Pro Max',
    'year': 2025,
    'color': 'Silver',
    'price': 1500
}

# 1. get metodi - kalit orqali qiymatni olish
print(phone.get('model')) # iPhone 17 Pro Max
print(phone.get('price')) # 1500
print(phone.get('battery')) # None (kalit majud emas)
print(phone.get("battery", "Kalit topilmadi")) # Kalit topilmadi

# 2. items() metodi - lug'at elementlarini (kalit, qiymat) juftlari sifatida olish
print(phone.items())
for key, value in phone.items():
    print(f"{key}: {value}")

telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310'
    }

for k, q in telefonlar.items():
    print(f"{k.title()}ning telefoni {q}")

# 3. keys() metodi - lug'aatning barcha kalitlarini olib beradi
print(phone.keys()) 
print(telefonlar.keys())

mahsulotlar = { # Do'kondagi mahsulotlar
    'olma':10000,
    'anor':20000,
    'uzum':40000,
    'anjir':25000,
    'shaftoli':30000
    }
# print(mahsulotlar.keys())
print("Do'kondagi mahsulotlar:")
for mahsulot in mahsulotlar.keys():
    print(mahsulot.title())

# 4. in operatori
# # 1. listda in opweratori qiymat mavjudligini tekshiradi
# fruits = ['olma', 'anor', 'uzum', 'anjir', 'shaftoli']
# print('olma' in fruits)
# print('tarvuz' in fruits)

# fruit = input("Qaysi meva yoqadi?")
# if fruit in fruits:
#     print(f"{fruit.title()} do'konimizda bor.")
# else:
#     print(f"{fruit.title()} do'konimizda yo'q.")


bozorlik = ['anor','uzum','non','baliq']
for mahsulot in mahsulotlar:
    print(mahsulot) # lig'atning kalitlari bo'ladi

for mahsulot in mahsulotlar:
    for mahsulot in bozorlik:
        print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")

print(sorted(mahsulotlar.keys())) # ['anjir', 'anor', 'olma', 'shaftoli', 'uzum']
print("Do'konimizdagi mahsulotlar:")
for mahsulot in sorted(mahsulotlar):
    print(mahsulot.title())

# 5, values() metodi - lug'atning barcha qiymatlarini oplish
print(phone.values())
print(telefonlar.values())

telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310',
    'hamida':'galaxy s9',
    'maryam':'huawei p30',
    'tohir':'iphone x',
    'umar':'iphone x'    
    }

print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
for tel in telefonlar.values():
    print(tel)

