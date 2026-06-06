# OOP - Object Oriented Programming(Obyektga yo'naltirilgan dasturlash)
# 1. Class(Objekt uchun shablon, qolip) va objekt(Shablondan yaratilgan narsa)
# 2. OOP ustunlari:
    # 1. Encapsulation - kapsulyatsiya, ma'lumotlarni va metodlarni bitta birlikda jamlash
    # 2. Inheritance - merosxo'rlik
    # 3. Polymorphism - ko'p shakllilik, bir nechta shaklga ega bo'lish
    # 4. Abstraction - abstraksiya

class Car:
    def __init__(self, model, color, price):
        self.model = model
        self.color = color
        self.price = price

    def start(self):
        return f"{self.model} is starting"
    
car1 = Car("BMW", "Black", 50000)
print(car1)  # BMW    
car1.start()
car2 = Car("Mercedes", "White", 60000)
print(car2)  # Mercedes
print(car2.start())  # Mercedes is starting