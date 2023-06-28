
# Вам предстоит решить две задачи и пройти код-ревью по ним.
# Сдавайте решения в Яндекс.Контест, а когда получите ОК по обеим задачам,
# — запакуйте решения в один архив и загрузите на ревью.
# В начале каждого решения в комментарии укажите ID успешной посылки,
# чтобы ревьюер мог удостовериться, что решение рабочее.


# Ближайший ноль
'''
n = int(input())
houses = list(map(int, input().split()))

result = [0] * n


nearest_zero = -1
for i in range(n):
    if houses[i] == 0:
        nearest_zero = i
    if nearest_zero >= 0:
        result[i] = i - nearest_zero


nearest_zero = n
for i in range(n-1, -1, -1):
    if houses[i] == 0:
        nearest_zero = i
    if nearest_zero < n:
        if result[i] == 0 or nearest_zero - i < result[i]:
            result[i] = nearest_zero - i

print(*result)
'''



