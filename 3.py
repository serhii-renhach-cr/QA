


# qqq = [64, 64, 65]
# asc_abc = sorted(qqq)
# A = pow(asc_abc[2], 2)
# B = pow(asc_abc[0], 2)
# C = pow(asc_abc[1], 2)
# a = asc_abc[2]
# b = asc_abc[0]
# c = asc_abc[1]
# if a + b > c and b + c > a and a + c > b:
#     P = a+b+c
#     p = P/2
#     S = (p*(p-a)*(p-b)*(p-c))*0.5
#     print(f"Периметр = {P} Площадь = {S}")
#     if A < B + C:
#         print('Остроугольный')
#     elif A == B + C:
#         print('Прямоугольный')
#     elif A > B + C:
#         print('Тупоугольный')
#     if a != b and b != c and c != a :
#         print('Разносторонний')
#     elif a == b != c or b == c != a or a == c != b:
#         print('Равнобедренный')
#     elif a == b and b == c and c == a:
#         print('Равносторонний')
#
# else:
#     print('Не может быть')


class Triangle():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


    def perimetr(self):
        abc = []
        abc.append(self.a)
        abc.append(self.b)
        abc.append(self.c)
        asc_abc = sorted(abc)
        a = asc_abc[2]
        b = asc_abc[0]
        c = asc_abc[1]
        if a + b > c and b + c > a and a + c > b:
            P = a + b + c
            print(f"Perimetr = {P}")
        else:
            print('Such a triangle cannot exist.')


    def square(self):
        abc = []
        abc.append(self.a)
        abc.append(self.b)
        abc.append(self.c)
        asc_abc = sorted(abc)
        a = asc_abc[2]
        b = asc_abc[0]
        c = asc_abc[1]
        if a + b > c and b + c > a and a + c > b:
            P = a + b + c
            p = P/2
            S = (p*(p-a)*(p-b)*(p-c))*0.5
            print(f"Square = {S}")
        else:
            print('Such a triangle cannot exist.')

    def type(self):
        abc = []
        abc.append(self.a)
        abc.append(self.b)
        abc.append(self.c)
        asc_abc = sorted(abc)
        A = pow(asc_abc[2], 2)
        B = pow(asc_abc[0], 2)
        C = pow(asc_abc[1], 2)
        a = asc_abc[2]
        b = asc_abc[0]
        c = asc_abc[1]
        if a + b > c and b + c > a and a + c > b:
            if A < B + C:
                print('Acute-angled')
            elif A == B + C:
                print('Rectangular')
            elif A > B + C:
                print('Obtuse')
            if a != b and b != c and c != a :
                print('Іcalene')
            elif a == b != c or b == c != a or a == c != b:
                print('Isosceles')
            elif a == b and b == c and c == a:
                print('Equilateral')

        else:
            print('Such a triangle cannot exist.')





#Triangle1 = Triangle(3, 4, 5)
#Triangle1 = Triangle(2, 3, 4)
#Triangle1 = Triangle(66, 67, 68)
#Triangle1 = Triangle(20, 20, 25)
#Triangle1 = Triangle(5, 6, 20)
#Triangle1 = Triangle('q', 'w', 'e')
#Triangle1 = Triangle(0, 0, 0)
#Triangle1 = Triangle(-2, -3, -5)
Triangle1.perimetr()
Triangle1.square()
Triangle1.type()
