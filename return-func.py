# def is_even(number):
#     if number % 2 == 0:
#         return "Juft"
#     else:
#         return "False"
    
# print(is_even(4)) # juft
# result = is_even(7)
# print(result)

# Ternary operator yordamida yuqoridagi funksiyani qisqartirish mumkin:
# syntax: value_if_true if condition else value_if_fal

def is_even(number):
    return "juft" if number % 2 == 0 else "toq"

print(is_even(4)) # juft
print(is_even(7)) # toq

volwes = ["a", "o", "i", "u", "e"]
def count_volwes(text):
    count = 0
    for char in text:
        if char == volwes[0] or char == volwes[1] or char == volwes[2] or char == volwes[3] or char == volwes[4]:
            count += 1
    return count
print(count_volwes("javaskrib"))
print(count_volwes("python"))

# string bo'yicha for loop ishlatish
# text = "Hello world"
# for char in text:
#     print(char)