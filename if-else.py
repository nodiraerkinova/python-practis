# age = int(input("Yoshingizni kiriting"))
# if age > 18:
#     print("Kirish huquqiga egasiz") 
# else: 
#     print("Siz hali yoshsz")    

# age = int(input("Yoshingizni kiriting"))
# if age > 16:
#      print("Paspotr olish huquqiga egasiz") 
# else: 
#      print("Siz hali pasport ololmaysiz")  

# number = float(input("Son kiriting"))
# if number > 0: 
#      print("Musbat son")
# else:
#      print("Manfiy son") 

# son = int(input("Son kiriting"))
# if son % 2 == 0 and son % 3 == 0:
#     print("6 ga bo'linadi")
# elsson    print("6 ga bo'linmaydso

# a = int(i3-sonni: "))
# b = int(input("2-tomonni kiriting: "))
# c = int(input("3-tomonni kiriting: "))

# if a + b > c and a + c > b and b + c > a:
#     print("Uchburchak bo'ladi")
# else:
#     print("Uchburchak bo'lmaydi") 

# a = int(input("1-tomonni kiriting: "))
# b = int(input("2-tomonni kiriting: "))
# c = int(input("3-tomonni kiriting: "))
# if a < b < c:
#     print("YES")
# else:
#     print("NO") 

# a = int(input("1-tomonni kiriting: "))
# b = int(input("2-tomonni kiriting: "))
# if a > b:
#     print(a)
# else:
#     print(a, b) 

# a = int(input("1-tomonni kiriting: "))
# b = int(input("2-tomonni kiriting: "))
# if a <= b:
#     a = 0
#     print(a , b)
# else:
#     print(a, b) 

# import math
# a = int(input("1-tomonni kiriting: "))
# b = int(input("2-tomonni kiriting: "))
# c = int(input("3-tomonni kiriting: "))
# if a>= b>= c:
#     print(2*a, 2*b, 2*c)
# else:
#     print(math.fabs(a), math.fabs(b), math.fabs(c))

# import math
# x = int(input("1-tomonni kiriting: "))
# y = int(input("2-tomonni kiriting: ")) 
# a = (x + y) / 2
# b = 2 * (x * y)
# if x > y:
#     y = a
#     x = b
# else:
#     x = b
#     y = a

#     print("%.1f" % x, "%.1f" % y) 

# ball = int(input("Balingizni kiriting: "))
# if ball < 56:
#     print("Siz imtihondan o'ta olmadingiz")
# elif ball >= 56 and ball < 70:
#     print("Siz imtihondan 3 baxo bn o'taing")
# elif ball >=70 and ball < 86:
#     print("Siz imtihondan 4 baxo bn o'taing")
# elif ball >= 86 and ball <= 100:
#     print("Siz imtihondan 5 baxo bn o'taing")
# else:
#     print("Iltimos 0 dan 100 gacha kiriting") 

# import math
# x = float(input("1-tomonni kiriting: "))
# y = float(input("2-tomonni kiriting: ")) 
# if x < 0 and y < 0:
#     print(math.fabs(x), math.fabs(y))
# elif x < 0 or y < 0:
#     print((x + 0.5), (y + 0.5)) 
# elif x > 0 and y > 0:
#     print(x, y) 

# import math 
# a = int(input("1-sonni kiriting: "))
# b = int(input("2-sonni kiriting: "))
# c = int(input("3-sonni kiriting: "))
# D = (b ** 2) +( 4 * a * c)
# if D < 0:
#     print("NO")
# else:
#     x1 = (-b + math.sqrt(D)) / (2 * a)
#     x2 = (-b - math.sqrt(D)) / (2 * a)
#     print("%.2f" % x1, "%.2f" % x2) 

# x = float(input("1-tomonni kiriting: "))
# y = float(input("2-tomonni kiriting: "))
# z = float(input("2-tomonni kiriting: "))
# if 1 <= x <= 3: 
#     print(x)
# if y >= 1 and y <= 3:
#     print(y) 
# if 1 <= z <= 3:
#     print(z) 

# x = int(input("1-tomonni kiriting: "))
# y = int(input("2-tomonni kiriting: "))
# z = int(input("2-tomonni kiriting: "))
# if x > 0:
#     x = x ** 2
# if y > 0:
#     y = y ** 2
# if z > 0:
#     z = z ** 2

# print(x, y, z) 

# 12.77, 15.88, -75, 18, 0, 89, 25
# max - engkatta => 89
# min - eng kichik => -75
# print(max(12.77, 15.88, -75, 18, 0, 89, 25))
# print(min(12.77, 15.88, -75, 18, 0, 89, 25))

# x = float(input("1-sonni kiriting: "))
# y = float(input("2-sonni kiriting: "))
# z = float(input("3-sonni kiriting: "))
# print(max(x, y, z), min(x, y, z)) 

# x = float(input("1-sonni kiriting: "))
# y = float(input("2-sonni kiriting: "))
# z = float(input("3-sonni kiriting: ")) 
# a = max(x + y + z, x, y, z) 
# b = min(x + y / 2, x, y, z) 
# print(a, b ** 2) 

# a = float(input("1-sonni kiriting: "))
# b = float(input("2-sonni kiriting: "))
# c = float(input("3-sonni kiriting: ")) 
# d = float(input("4-sonni kiriting: ")) 
# x = max(a, b, c, d)
# y = min(a, b, c, d)
# if a <= b <= c <= d:
#     a = b = c = d = x 
# else:
#     a = b = c = d = x
    
# print(a, b, c, d) 

# x = float(input("1 - sonni kiriting: "))
# y = float(input("2 - sonni kiriting: "))
# a = (x + y) / 2
# b = 2 * x * y
# if x > y:
#     x = a
#     y = b
# elif x < y:
#     x = b
#     y = a
# print(int(x), int(y)) 

x = float(input("1 - sonni kiriting: "))
y = float(input("2 - sonni kiriting: "))
z = float(input("3 - sonni kiriting: "))
a = min(x, y, z)
if x < 1 and y < 1 and z < 1:
    if a == x:
        x = (y + z) / 2
    elif a == y:
        y = (x + z) / 2
    else:
        z = (x + y) / 2
print(x, y, z)  