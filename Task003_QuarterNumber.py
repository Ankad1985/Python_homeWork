# 3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int(input("Введите значение Х: "))
y = int(input("Введите значение Y: "))
if x > 0 and y > 0:
    print("Точка находится в 1 четверти")
if x < 0 and y > 0:
    print("Точка находится во 2 четверти")
if x < 0 and y < 0:
    print("Точка находится в 3 четверти")
if x > 0 and y < 0:
    print("Точка находится в 4 четверти")
if x == 0 or y == 0:
    print("Введите значения Х и У больше 0")
