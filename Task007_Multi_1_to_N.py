# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# 1 - 1 * 1, 2 - 1 * 2, 3 - 1 * 2 * 3, 4 - 1 * 2 * 3 * 4 и т.д.
# - 4 -> [1, 2, 6, 24]
# - 6 -> [1, 2, 6, 24, 120, 720]

# number = int(input("Введите число N: "))
# i = 1
# multi = 1
# while i <= number:
#     multi *= i
#     print(multi,end= ' ')
#     i += 1

number = int(input("Введите число N: "))
multi = 1
for i in range(1, number + 1):
    multi *= i
    print(multi, end=" ")
    