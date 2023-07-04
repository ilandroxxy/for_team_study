# region 2. Ввод-вывод данных

# 2.5 Целочисленная арифметика. Часть 2

# Тема урока: работа с целыми числами

# 1. Операция возведения в степень
# 2. Операция нахождения остатка
# 3. Операция целочисленного деления
# 4. Обработка цифр числа
# 5. Решение задач

# region 1. Операция возведения в степень:

# Оператор возведения в степень a ** n возводит число a в степень n.

# Обратите внимание: оператор возведения в степень ** может возводить не только в положительную степень,
# но и в отрицательную.

# Аналогично, основание степени a также может быть числом отрицательным.

# Обратите внимание: оператор возведения в степень (**) является правоассоциативным
# (значение выражения вычисляется справа налево) в соответствии с правилами математики.
# Таким образом, выражение x ** y ** z вычисляется как x ** (y ** z)

"""
print(2**6)  # Ответ: 64
"""

# endregion
# region 2. Операция нахождения остатка:

# Оператор деления с остатком возвращает остаток от деления двух целых чисел.

# Примечание 1. Оператор нахождения остатка очень полезен при решении многих задач.
# Например, число делится на n нацело тогда и только тогда, когда остаток от деления на n равен 0.

# Примечание 2. Операторы // и % имеют такой же приоритет, как и операторы умножения и обычного деления.

# Примечание 3. Наивысший приоритет имеет оператор возведения в степень **.

# Примечание 4. Полезно прочитать про модулярную арифметику в математике.

# Примечание 5. Обратите внимание: результатом деления n % m при n < m является число n.
# Например, 5 % 9 = 5, 3 % 13 = 3 и т.д.

# endregion
# region 3. Операция целочисленного деления:

# Для положительных чисел оператор целочисленного деления ведёт себя как обычное деление,
# за исключением того, что он отбрасывает десятичную часть результата.
# Рассмотрим работу данного оператора на примерах:
"""
print(10 // 3)  # 3
print(10 // 4)  # 2
print(10 // 5)  # 2
print(10 // 6)  # 1
print(10 // 12)  # 0
"""

# При делении отрицательных чисел необходимо помнить, что результат целочисленного деления не превосходит частное.
# Другими словами, округление берётся в меньшую сторону (число -4 меньше, чем число -3):
"""
print(10 // 3)  # 3 (округление в меньшую сторону)
print(-10 // 3)  # -4 (округление в меньшую сторону)
"""

# endregion
# region 4. Обработка цифр числа:

# Последняя цифра: (num % 10**1) // 10**0;
# Предпоследняя цифра: (num % 10**2) // 10**1;
# Предпредпоследняя цифра: (num % 10**3) // 10**2;

# Вторая цифра: (num % 10**n-1) // 10**n-2;
# Первая цифра: (num % 10**n) // 10**n-1.

# endregion
# region 5. Решение задач:

# Геометрическая прогрессия
'''
b1 = int(input())
q = int(input())
n = int(input())

res = b1 * (q ** (n-1))
print(res)
'''
# Вы получили: 5 баллов из 5


# Номер купе 🌶️
'''
num = int(input())

def F(num):
    if 1 <= num <= 4:
        return 1
    elif 5 <= num <= 8:
        return 2
    elif 9 <= num <= 12:
        return 3
    elif 13 <= num <= 16:
        return 4
    elif 17 <= num <= 20:
        return 5
    elif 21 <= num <= 24:
        return 6
    elif 25 <= num <= 28:
        return 7
    elif 29 <= num <= 32:
        return 8
    elif 33 <= num <= 36:
        return 9
    
print(F(num))
'''
# Вы получили: 10 баллов из 10


# Пересчет временного интервала
'''
time = int(input())
hours = time // 60
minute = time % 60

print(f'{time} мин - это {hours} час {minute} минут.')
'''
# Вы получили: 5 баллов из 5


# Трехзначное число
'''
x3 = int(input())
M = [int(i) for i in str(x3)]
summ = sum(M)
prod = M[0] * M[1] * M[2]
print(f'Сумма цифр = {summ}')
print(f'Произведение цифр = {prod}')
'''
# Вы получили: 5 баллов из 5


# Перестановка цифр
'''
x = int(input())
M = [int(i) for i in str(x)]

print(M[0], M[1], M[2], sep='')
print(M[0], M[2], M[1], sep='')
print(M[1], M[0], M[2], sep='')
print(M[1], M[2], M[0], sep='')
print(M[2], M[0], M[1], sep='')
print(M[2], M[1], M[0], sep='')
'''
# Вы получили: 5 баллов из 5


# Четырёхзначное число
'''
x = int(input())
M = [int(i) for i in str(x)]

print(f'Цифра в позиции тысяч равна {M[0]}')
print(f'Цифра в позиции сотен равна {M[1]}')
print(f'Цифра в позиции десятков равна {M[2]}')
print(f'Цифра в позиции единиц равна {M[3]}')
'''
# Вы получили: 5 баллов из 5


# endregion


# endregion
# region 3. Итоговая работа на ввод-вывод данных

''''''
# endregion

# region 4. Условный оператор

# region 4.1 Выбор из двух
# region Теория

# Транзитивность

# Операция равенства является транзитивной.
# Это означает, что если a == b и b == c, то из этого следует, что a == c.
# Именно поэтому предыдущий код, проверяющий равенство трёх переменных, работает как полагается.

# Из курса математики вам могут быть знакомы другие примеры транзитивных операций:
# Отношение порядка: если a > b и b > c, то a > c
# Параллельность прямых: если a || b и b || c, то a || c
# Делимость: если a делится на b и b делится на c, то a делится на c

# Наглядно транзитивность отношения порядка можно понять на таком примере:
# если сосед слева старше вас (a>b), а вы старше соседа справа (b>c),
# то сосед слева точно старше соседа справа (a>c).

# Операция неравенства (!=), в отличие от операции равенства (==), является нетранзитивной.
# То есть из того, что a != b и b != c,вовсе не следует, что a != c.
# Действительно, если вас зовут не так, как соседа слева и не так, как соседа справа,
# то нет гарантии, что у обоих соседей не окажутся одинаковые имена.

# Таким образом, следующий код вовсе не проверяет тот факт, что все три переменные различны:
'''
if a != b != c:
    print('числа не равны')
else:
    print('числа равны')
'''
# Код, проверяющий, что значения трёх переменных различны, мы научимся писать немного позже.

# endregion
# region Решение задач

# Пароль
'''
pass1 = str(input())
pass2 = str(input())
if pass1 == pass2:
    print(f'Пароль принят')
else:
    print(f'Пароль не принят')
'''
# Вы получили: 5 баллов из 5


# Четное или нечетное?
'''
x = int(input())
if x % 2 == 0:
    print(f'Четное')
else:
    print(f'Нечетное')
'''
# Вы получили: 5 баллов из 5


# Соотношение
'''
x = int(input())
M = [int(i) for i in str(x)]

if (M[0] + M[3]) == (M[1] - M[2]):
    print(f'ДА')
else:
    print(f'НЕТ')
'''
# Вы получили: 5 баллов из 5


# Роскомнадзор
'''
age = int(input())
if age >= 18:
    print(f'Доступ разрешен')
else:
    print(f'Доступ запрещен')
'''
# Вы получили: 5 баллов из 5


# Арифметическая прогрессия
'''
x1 = int(input())
x2 = int(input())
x3 = int(input())

if (x2 - x1) + x2 == x3:
    print(f'YES')
else:
    print(f'NO')
'''
# Вы получили: 5 баллов из 5


# Наименьшее из двух чисел
'''
x1 = int(input())
x2 = int(input())

if x1 > x2:
    print(x2)
else:
    print(x1)
'''
# Вы получили: 5 баллов из 5


# Наименьшее из четырёх чисел 🌶️
'''
M = []
x1 = int(input())
x2 = int(input())
x3 = int(input())
x4 = int(input())

M.append(x1)
M.append(x2)
M.append(x3)
M.append(x4)

print(min(M))
'''
# Вы получили: 10 баллов из 10


# Возрастная группа
'''
x = int(input())
if x <= 13:
    print(f'детство')
if 14 <= x <= 24:
    print(f'молодость')
if 25 <= x <= 59:
    print(f'зрелость')
if x >= 60:
    print(f'старость')
'''
# Вы получили: 5 баллов из 5


# Только + 🌶️
'''
M = []

x1 = int(input())
x2 = int(input())
x3 = int(input())

if x1 > 0:
    M.append(x1)
if x2 > 0:
    M.append(x2)
if x3 > 0:
    M.append(x3)

print(sum(M))
'''
# Вы получили: 10 баллов из 10

# endregion

# endregion
# region 4.2 Логические операции

# region Решение задач

# Какое значение будет выведено на экран после выполнения следующей программы, если с клавиатуры введено число 7?
'''
a = int(input())
if a >= 2 and a <= 17:
    b = 3
    p = a * a + b * b
else:
    b = 5
p = (a + b) * (a + b)
print(p)
'''
# Ответ: 100
# Вы получили: 1 балл из 1


# Принадлежность 1
'''
x = int(input())
if -1 < x < 17:
    print(f'Принадлежит')
else:
    print(f'Не принадлежит')
'''
# Вы получили: 5 баллов из 5


# Принадлежность 2
'''
x = int(input())
if x <= -3 or x >= 7:
    print(f'Принадлежит')
else:
    print(f'Не принадлежит')
'''
# Вы получили: 5 баллов из 5


# Принадлежность 3
'''
x = int(input())
if -30 < x <= -2 or 7 < x <= 25:
    print(f'Принадлежит')
else:
    print(f'Не принадлежит')
'''
# Вы получили: 5 баллов из 5


# Красивое число 🌶️
'''
x = int(input())
if (len(str(x)) == 4 and x % 17 == 0) or (len(str(x)) == 4 and x % 7 == 0):
    print(f'YES')
else:
    print(f'NO')
'''
# Вы получили: 10 баллов из 10


# Неравенство треугольника
'''
M = []
x1 = int(input())
x2 = int(input())
x3 = int(input())

M.append(x1)
M.append(x2)
M.append(x3)

if max(M) < (sum(M) - max(M)):
    print(f'YES')
else:
    print(f'NO')
'''
# Вы получили: 5 баллов из 5


# Високосный год
'''
x = int(input())
if (x % 4 == 0 and x % 100 != 0) or x % 400 == 0:
    print(f'YES')
else:
    print(f'NO')
'''
# Вы получили: 5 баллов из 5


# Ход ладьи
'''
start1 = int(input())  # Столбец
start2 = int(input())
kon1 = int(input())  # Строка
kon2 = int(input())

if (start1 != kon1 and start2 == kon2) or (start1 == kon1 and start2 != kon2):
    print(f'YES')
else:
    print(f'NO')
'''
# Вы получили: 5 баллов из 5


# Ход короля 🌶️
'''
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if -1 <= x1-x2 <= 1 and -1 <= y1-y2 <= 1:
    print('YES')
else:
    print('NO')
'''
# Вы получили: 10 баллов из 10

# endregion

# endregion
# region 4.3 Вложенные и каскадные условия

# region Решение задач

# Гонка спидстеров
'''
zum = int(input())
flash = int(input())

if zum > flash:
    print(f'NO')
elif flash > zum:
    print(f'YES')
else:
    print(f"Don't know")
'''
# Вы получили: 5 баллов из 5


# Вид треугольника
'''
M = []
x1 = int(input())
x2 = int(input())
x3 = int(input())

M.append(x1)
M.append(x2)
M.append(x3)

if len(set(M)) == 1:
    print(f'Равносторонний')
elif len(set(M)) == 2:
    print(f'Равнобедренный')
else:
    print(f'Разносторонний')
'''
# Вы получили: 5 баллов из 5


# Среднее число
'''
M = []
x1 = int(input())
x2 = int(input())
x3 = int(input())

M.append(x1)
M.append(x2)
M.append(x3)

Ms = sorted(M)
print(Ms[1])
'''
# Вы получили: 5 баллов из 5


# Количество дней
'''
x = int(input())
if x == 1 or x == 3 or x == 5 or x == 7 or x == 8 or x == 10 or x == 12:
    print(31)
elif x == 2:
    print(28)
else:
    print(30)
'''
# Вы получили: 5 баллов из 5