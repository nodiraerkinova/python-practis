text = "Hey guys"
# print(len(text)) # 8
# # String ichidagi harflar va bo'shliq ham hisobga olinadi
# # String ichidagi belgilarning indekslari 0 dan boshlanadi
# print(text[0]) # H
# print(text[1]) # e      
# print(text[2]) # y
# print(text[3]) # (space)
# print(text[4]) # g
# print(text[5]) # u
# print(text[-1]) # !      
# print(text[-2]) # e
# length = len(text)
# # oxirgi belgini olish uchun length - 1 indeksidan foydalanamiz
# print(text[length - 1]) # !

# for loop yordamida string ichidagi harflarni alohida-alohida chiqarish
# 1-usul
# for char in text:
#     print(char)

# 2-usul
for index in range(len(text)):
    print(index, text[index])

# in operratori yordamida string ichida ma'lum bir belgi yoki so'z bor-yo'qligini tekshirish
print("welcome" in text) # True 
