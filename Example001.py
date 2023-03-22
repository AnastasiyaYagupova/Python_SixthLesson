## F = int(input("Введите первое число прогрессии "))
## R = int(input("Введите разность прогрессии "))
## N = int(input("Введите размер массива "))

n = int(input('Input n ')) #общее кол-во эл-в
x = int(input('Input a[0] ')) #первое число
d = int(input('Input d ')) #шаг
print(*range(x, x + d * n, d))