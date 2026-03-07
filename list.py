# # List - ro'yxat
# user1 = "Bekhruz" 
# user2 = "Maftuna"
# print(user1)
# print(type(user2)) # str
# users = ['Gulyora', "G'ulomjo", 'John', "Margaritta"]
# # List elelmantlari indexlanadi
# # Dasturlashda indexlash 0 dan boshlanadi
# # List elementini olish
# firet_element = users[0]
# third_element = users[2]
# print(firet_element, third_element, users[3])
# print(type(users)) # list 
# mixed_date = ['test', 12, True, -5.75, False, ['hey', 'xi'], 'py', 'js', 'c++', 25] 
# # List uzunligi (length of list) - ro'yxatdagi elemantlar soni
# print(len(users))
# print(len(mixed_date))
# print(mixed_date[5]) 
# # first elelment
# print(mixed_date[0])
# # last element
# length = len(mixed_date)
# print(mixed_date[length - 1]) 
# # List elementini o'zgartirish
# mixed_date[2] = False 
# print(mixed_date[2]) 
# # Element qo'shish 
# users.append('valeriy') 
# print(users) 
# users.insert(0, 'Malhiyoxon') 
# print(users)
# users.insert(2,'Cristiano') 
# print(users)
# users.insert(len(users) - 1, 'Nodir') 
# print(users) 
# # Elementni o'chirish
# del users[4]
# print(users)
# users.remove('Cristiano')
# print(users) 

# Listdan element sug'rib olish
# List.pop(index?)
# deleteElement = users.pop(1)
# print(deleteElement)
# print(users)

# lastelement = users.pop()
# print(lastelement)
# print(users) 

# Practis 2
ismlar = ['Abror', 'Maxmur', 'Bobur']
print("Salom" + ismlar[0], "bugun choyxona bormi?")
print(ismlar[1], "choyxonaga boramizmi") 

t_shaxslar= ['Imom buxoriy', 'Al xorazmiy', 'Amir Temur']
z_shaxslar = ['Bil Gates', 'Shavkat Mirziyoyev', 'Vini Jr']
print("Men tarixiy shaxslardan" + t_shaxslar[0] + 'bilan', "zamonaviy shaxslardan esa" + z_shaxslar[1] + "bilan suhbatlashgan bo'lar edim" )
