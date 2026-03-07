# import math
# a = int(input("1-sonni kiriting: "))
# x = float(input("2-sonni kiriting: "))
# y = float(input("3-sonni kiriting: "))
# b = math.sqrt(math.exp(x * y) - x * math.sin(a * x) - (math.pow(x, 2) + 2) / (math.fabs(x) + 5))
# c = math.sqrt(math.log(math.pow(x, 2) + 2) + 5)
# w2 = b + c
# print(w2)

# import math
# a = int(input("1-sonni kiriting: "))
# x = float(input("2-sonni kiriting: "))
# b = x * math.sin(x / 2 + x / 3 + x / 4)
# c = math.log10(math.pow(x, 2) - 2) + math.pow(3, a)
# d = math.cos(x + 3) * math.sin(x + 3) + 8
# bb1 = b + c / d
# print(bb1) 

# import math
# x = float(input("1-sonni kiriting: "))
# a = 2 * math.tan(x + 2) - math.cos(x + math.pow(2, x))
# b = 1 + math.pow(math.cos(x + 2), 2)
# c = math.sin(math.pow(x, 2))
# d = math.pow(x, 2) + 3
# f = math.sqrt(a / b)
# AA = f + (c / d)
# print("%.2f" % AA) 

# import math
# a = int(input("1-sonni kiriting: "))
# x = float(input("2-sonni kiriting: "))
# y = float(input("3-sonni kiriting: "))
# b = math.pow(y, 2) + math.exp(x)
# c = math.sqrt(math.exp(x) + a / (math.pow(x, 2) + 2))
# d = math.pow(math.cos(x), 2) / math.sin(math.pow(x, 2))
# e = math.pow(math.cos(x), 3)
# tt = math.sqrt(b + c + d) + e
# print("%.2f" % tt) 

import math
x = int(input("1 -sonni kiriting: "))
y = float(input("2 -sonni kiriting: "))
z = float(input("3 -sonni kiriting: "))
a = math.pow(2, -x) * math.sqrt(x + (math.fabs(y) + 2) ** 0.25)
b = math.pow((math.exp(x-1) / math.sin(z + 2) + 2), 1/3)
AF = a * b
print("%.2f" % AF) 
