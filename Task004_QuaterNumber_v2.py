# 4. Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

quaterNumber = int(input("Введите номер четверти: "))

if quaterNumber == 1:
    print("х > 0 до ∞; y > 0 до ∞")
elif quaterNumber == 2:
    print("х < 0 до -∞; y > 0 до ∞")
elif quaterNumber == 3:
    print("х < 0 до -∞; y < 0 до -∞")
elif quaterNumber == 4:
    print("х > 0 до ∞; y < 0 до -∞")
else:
    print("Введите значение от 1 до 4")
