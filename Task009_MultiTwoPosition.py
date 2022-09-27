# 4. Напишите программу, которая принимает на вход 2 числа. Задайте список из N элементов,
# заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях(не индексах).
# Position one: 1
# Position two: 3
# Number of elements: 5
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 15

numberOfElements = int(input("Введите количество элементов N: "))
elementsArray = []
positionOne = int(input("Введите позицию 1 элемента: "))
positionTwo = int(input("Введите позицию 2 элемента: "))

if numberOfElements < 0:
        numberOfElements = numberOfElements * -1
elif positionOne > numberOfElements * 2 + 1 or positionTwo > numberOfElements * 2 + 1:
    print("Введены некорректные данные")
elif positionOne <= 0 or positionTwo <= 0:
    print("Номер позиции должен быть больше нуля")
else:        
    for i in range(-numberOfElements, numberOfElements + 1):    
        elementsArray.append(i)

multi = elementsArray[positionOne - 1] * elementsArray[positionTwo - 1]

print("Полученный диапазон от -N до N:", elementsArray, end="")
print("\nПроизведение элементов на указанных позициях:", multi)
