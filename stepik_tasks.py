"""
Документация к файлу stepik_tasks:

Этот файл предназначен для работы с задачами Stepik
Курс: "Поколение Python для профессионалов"
"""

# region Функция index_of_nearest()
# Реализуйте функцию index_of_nearest(), которая принимает два аргумента в следующем порядке:
#
# numbers — список целых чисел
# number — целое число
# Функция должна находить в списке numbers ближайшее по значению число к числу number и возвращать его индекс.
# Если список numbers пуст, функция должна вернуть число −1.
'''
def index_of_nearest(numbers, number):
    nearby_number = -1
    mini = 9999999
    for i in range(len(numbers)):
        if abs(number - numbers[i]) < mini:
            mini = abs(number - numbers[i])
            nearby_number = i
    return nearby_number


print(index_of_nearest([7, 13, 3, 5, 18], 0))
print(index_of_nearest([9, 5, 3, 2, 11], 4))
print(index_of_nearest([7, 5, 4, 4, 3], 4))
'''
# endregion Функция index_of_nearest()

# region Тимур, Артур и новый курс
'''
d1 = int(input())
d2 = int(input())
d3 = int(input())

way1 = d1 + d3 + d2
way2 = d1 + d1 + d2 + d2
way3 = d1 + d3 + d3 + d1
way4 = d2 + d3 + d3 + d2
print(min(way4, way3, way2, way1))
'''
# endregion Тимур, Артур и новый курс

# region Схожие буквы
# В русском и английском языках есть буквы, которые выглядят одинаково.
# Вот список английских букв "AaBCcEeHKMOoPpTXxy",
# а вот их русские аналоги "АаВСсЕеНКМОоРрТХху".
# Напишите программу, которая для трёх букв из данных списков букв определяет,
# русские они, английские или и те и другие (смесь русских и английских букв).
'''
ru = "АаВСсЕеНКМОоРрТХху"
en = "AaBCcEeHKMOoPpTXxy"
alphabet = ru + en
a, b, c = [input() for _ in range(3)]
if all(x in ru for x in [a, b, c]):
    print('ru')
elif all(x in en for x in [a, b, c]):
    print('en')
else:
    print('mix')
'''
# endregion Схожие буквы

# region Переворатор
# Дана последовательность натуральных чисел от 1 до n.
# Напишите программу, которая сначала располагает в обратном
# порядке часть элементов этой последовательности от элемента
# с номером X до элемента с номером Y, а затем от элемента
# с номером A до элемента с номером B.
'''
n, X, Y, A, B = [int(i) for i in input().split()]
numbers = [i for i in range(1, n+1)]
new_numbers = numbers[:X-1] + numbers[X-1:Y][::-1] + numbers[Y:]
new_numbers_2 = new_numbers[:A-1] + new_numbers[A-1:B][::-1] + new_numbers[B:]
print(*new_numbers_2)
'''
# endregion Переворатор

# region Более одного
# Дана последовательность неотрицательных целых чисел.
# Напишите программу, которая выводит те числа, которые
# встречаются в данной последовательности более одного раза.
'''
numbers = [int(i) for i in input().split()]
result = set()
for num in numbers:
    if numbers.count(num) > 1:
        result.add(num)
print(*sorted(result))
'''
# endregion Более одного

# Таблица-2
# Дано натуральное число (n≤ 9).
# Напишите программу, которая печатает таблицу размером n×5,
# где в i-ой строке указано число i (числа отделены одним пробелом).
'''
n = int(input())
for i in range(1, n+1):
    for j in range(5):
        print(i, end=' ')
    print()
'''


# Численный треугольник 2
# Дано натуральное число n.
# Напишите программу, которая печатает численный
# треугольник с высотой равной n, в соответствии с примером:
'''
n = int(input())
count = 1
for i in range(1, n+1):
    for j in range(1, i+1):
        print(count, end=' ')
        count += 1
    print()
'''


# Цифровой корень
# На вход программе подается натуральное число n.
# Напишите программу, которая находит цифровой корень данного числа.
# Цифровой корень числа n получается следующим образом:
# если сложить все цифры этого числа, затем все цифры найденной
# суммы и повторять этот процесс до тех пор, пока
# в результате не будет получено однозначное число (цифра),
# которое и называется цифровым корнем изначального числа.
'''
n = int(input())
while not(0 <= n <= 9):
    summ = 0
    while n > 0:
        summ += n % 10
        n //= 10
    n = summ
print(n)
'''
