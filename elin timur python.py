while True:
    d=int(input("Введите трехзначное число или выше = "))
    if d > 99:
     print("true");
     break;
    else:
     print("false")

#Begin3◦. Даны стороны прямоугольника a и b. Найти его площадь S = a·b и периметр P = 2·(a + b).
  
x=int(input('введите щироту = '))
y=int(input('введите длинну = '))
d = (x + y) * 2
print(d)

#Begin4◦. Дан диаметр окружности d. Найти ее длину L = π·d. В качествезначения π использовать 3.14

f=3.14
a=int(input('введите длинну = '))
l = f * a
print("длинна окружности = ",l)

#Begin5◦. Дана длина ребра куба a. Найти объем куба V = a3 и площадь егоповерхности S = 6·a2.

w=int(input("введите длинну ребра = "))
v = w **3
print("обьем куба = ",v)
e = 6 * w**2
print("площадь поверхности куба = ",e)

#Begin6◦. Даны длины ребер a, b, c прямоугольного параллелепипеда. Найтиего объем V = a·b·c и площадь поверхности S = 2·(a·b + b·c + a·c).

t=int(input("введите длинну = "))
i=int(input("введите длинну ширину = "))
o=int(input("введите длинну высоту = "))
u = t * i * o
print("обьем прямоугольника = ",u)
e = 2 * (t * i + i * o + t * o)
print("площадь поверхности прямоугольника = ",e)

#Begin7◦. Найти длину окружности L и площадь круга S заданного радиуса R:L = 2·π·R, S = π·R2

f=3.14
a=int(input('введите длинну = '))
r = a / 2
l = 2 * f * r
print("длинна окружности = ",l)
h = f * r**2
print("площадь круга = ",h)

#Begin8◦. Даны два числа a и b. Найти их среднее арифметическое: (a + b)/2.

x=int(input('введите число = '))
y=int(input('введите число = '))
d = (x + y) / 2
print("среднее арифметическое = ",d)

#Begin9◦. Даны два неотрицательных числа a и b. Найти их среднее геометрическое, то есть квадратный корень из их произведения: √a·b.

import math
g=int(input("введите число = "))
y=int(input('введите число = '))
print(math.sqrt(g * y))

#Begin10◦. Даны два ненулевых числа. Найти сумму, разность, произведение ичастное их квадратов.

g=int(input("введите число = "))
y=int(input('введите число = '))
g=g**2
y=y**2
i = g + y
p = g - y
l = g / y
a = g * y
print("сумма = ",i)
print("разность = ",p)
print("частное = ",l)
print("произведение = ",a)

#Begin11◦. Даны два ненулевых числа. Найти сумму, разность, произведение ичастное их модулей.

g=int(input("введите число = "))
y=int(input('введите число = '))
g=(math.fabs(g))
y=(math.fabs(y))
i = g + y
p = g - y
l = g / y
a = g * y
print("сумма = ",i)
print("разность = ",p)
print("частное = ",l)
print("произведение = ",a)

#Begin12◦. Даны катеты прямоугольного треугольника a и b. Найти его гипотенузу c и периметр P:c =√a2 + b2, P = a + b + c.

g=int(input("введите первый катет = "))
y=int(input('введите второй катет = '))
g=g**2
y=y**2
c = (math.sqrt(g * y))
print(c)
p = y + g + c
print(p)

#Begin13◦. Даны два круга с общим центром и радиусами R1 и R2 (R1 > R2).Найти площади этих кругов S1 и S2, а также площадь S3 кольца, внешнийрадиус которого равен R1, а внутренний радиус равен R2:S1 = π·(R1)2, S2 = π·(R2)2, S3 = S1 − S2.

f=3.14
while True:
    print("первый катет дожен быть выше второго")
    g=int(input("введите первый катет = "))
    y=int(input('введите второй катет = '))
    if g > y:
     break
    else:
     continue
h = f * g**2
f = f * y**2
d = h - f
print(h)
print(f)
print(d)

#Begin14◦. Дана длина L окружности. Найти ее радиус R и площадь S круга,ограниченного этой окружностью, учитывая, что L = 2·π·R, S = π·R2. Вкачестве значения π использовать 3.14.

f=3.14
a=int(input('введите длинну = '))
r = a / 2
l = 2 * f * r
print("радиус = ",r)
h = f * r**2
print("площадь круга = ",h)

#Begin15◦. Дана площадь S круга. Найти его диаметр D и длину L окружности,ограничивающей этот круг, учитывая, что L = 2·π·R, S = π·R2. В качествезначения π использовать 3.14.

f=3.14
a=int(input('введите площадь круга = '))
h = a / f
l = 2 * f * h
print("длинна окружности = ",l)
