# 'Задача' №1
# Поработайте с переменными, создайте несколько, выведите на экран.
# Запросите у пользователя некоторые числа и строки и сохраните в переменные,
# затем выведите на экран.

a = 7
b = 'whatever text'
c = 3.14
d = c != 3.13
print('a =', a, '  type:', type(a))
print('b =', b, '  type:', type(b))
print('c =', c, '  type:', type(c))
print('d =', d, '  type:', type(d))
string1 = input("Введите первую строку ")
number1 = int(input("Введите первое число "))
string2 = input("Введите вторую строку ")
number2 = int(input("Введите второе число "))
print("Вывод данных - %10s %5d %10s %5d" % (string1, number1, string2, number2))

# 'Задача' №2
# 'Пользователь вводит время в секундах.'
# 'Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.'
# 'Используйте форматирование строк.'
time = int(input('Введите время в секундах '))
hours = time // 3600
minutes = (time - hours * 3600) // 60
seconds = time - (hours * 3600 + minutes * 60)
print(f'Время в формате чч:мм:сс   {hours} : {minutes} : {seconds}')

# 'Задача' №3
# 'Узнайте у пользователя число n.'
# 'Найдите сумму чисел n + nn + nnn.'
# 'Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.'
n = int(input('Введите однозначное число: '))
total = (n + int(str(n) + str(n)) + int(str(n) + str(n) + str(n)))
print('Сумма чисел n + nn + nnn - %d' % total)

# 'Задача' №4
# 'Пользователь вводит целое положительное число.'
# 'Найдите самую большую цифру в числе.'
# 'Для решения используйте цикл while и арифметические операции.'
n = abs(int(input('Введите целое положительное число: ')))
max = n % 10
while n >= 1:
    n = n // 10
    if n % 10 > max:
        max = n % 10
    if n > 9:
        continue
    else:
        print('Максимальное значение в числе: ', max)
        break

# 'Задача' №5
# 'Запросите у пользователя значения выручки и издержек фирмы.'
# 'Определите, с каким финансовым результатом работает фирма.'
# 'Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки.'
# 'Выведите соответствующее сообщение.'
profit = float(input('Введите выручку фирмы: '))
costs = float(input('Введите издержки фирмы: '))
if profit > costs:
    print('фирма работает с прибылью')
elif profit == costs:
    print('фирма работает в ноль')
else:
    print('фирма работает в убыток')

# 'Задача' №6
# 'Если фирма отработала с прибылью, вычислите рентабельность выручки.'
# 'Это отношение прибыли к выручке.'
# 'Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчёте на одного сотрудника.'
profit = float(input('Введите выручку фирмы: '))
costs = float(input('Введите издержки фирмы: '))
if profit > costs:
    print(f'фирма работает с прибылью. Рентабельность выручки составила: {profit / costs:.2f}')
    workers = int(input('Введите количество сотрудников фирмы: '))
    print(f'прибыль в расчете на одного сторудника сотавила {profit / workers:.2f}')
elif profit == costs:
    print('фирма работает в ноль')
else:
    print('фирма работает в убыток')

# 'Задача' №7
# 'Спортсмен занимается ежедневными пробежками.'
# 'В первый день его результат составил a километров.'
# 'Каждый день спортсмен увеличивал результат на 10% относительно предыдущего.'
# 'Требуется определить номер дня, на который результат спортсмена составит не менее b километров.'
# 'Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.'
# 'Например: a = 2, b = 3.'
# 'Результат:'
# '1-й день: 2'
# '2-й день: 2,2'
# '3-й день: 2,42'
# '4-й день: 2,66'
# '5-й день: 2,93'
# '6-й день: 3,22'
# 'Ответ: на шестой день спортсмен достиг результата — не менее 3 км.'
a = int(input('Введите результат 1 дня в км: '))
b = int(input('Введите общий желаемый результат в км: '))
result_days = 1
result_km = a
while result_km < b:
    a = a + 0.1 * a
    result_days += 1
    result_km = result_km + a
    print(f'Достижение результата на %.d день' % result_days)
