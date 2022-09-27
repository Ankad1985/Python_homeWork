# 5. ** Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]


import random

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Исходный масссив:", numbers)
numbersLenght = len(numbers)
for i in range(numbersLenght):
    randomIndex = random.randint(0, numbersLenght - 1)
    temp = numbers[i]
    numbers[i] = numbers[randomIndex]
    numbers[randomIndex] = temp
print("Перемешанный массив:", numbers)
