# 5. Напишите программу, которая принимает на вход координаты двух точек и находит
# расстояние между ними в 2D пространстве.


from math import sqrt


x1 = int(input("Введите координату Х1 для первой точки: "))
y1 = int(input("Введите координату У1 для первой точки: "))
x2 = int(input("Введите координату Х2 для второй точки: "))
y2 = int(input("Введите координату Y2 для первой точки: "))

distance = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
distance = round(distance, 3)
print('Расстояние между точками в 2D равно:',end= " ")
print (distance)
