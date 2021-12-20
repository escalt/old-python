# 1) This file created, for learning, programming language Python_3.# |
# 2) Lessons_Part #1 -> 48 basic lessons Python.                      |
# 3) Lessons_Part #2 -> 24 lessons, graphic library TKINTER.          |
# ---------------------------------------------------------------------

"""Study lessons, Part #1 -> 48 lessons."""

# Lesson #1 (Introduction)
"""
# Basic info about Python Lang.
"""

# Lesson #2 (Install Python)
"""
#Have bin install, python intrpritator 3.8
"""

# Lesson #3 (Install (IDE)-IDLE PyCharm)
"""
#Have bin install, IDLE PyCharm for...
#And can, use interpritator Python from CMD
#just use command (D:\\SomeFolder>python fileCode.py)
"""

# Lesson #4 (Syntax Python)
"""
print('Hello, World')
print('Hello, World_1');print('Hello, World_2')
# Это однострочный комментарий
'''
Это многострочный комментарий
'''
# Открывающие-закрывающие скобки, ..не нужны
# Пробелы, табуляця,.. зарезервированны, вместо скобок
"""

# Lesson #5 (Number's and Arithmetic operator's)
"""
# Arithmetic operator's
'''
----------
(+)  Сложение-Суммирует значения слева и справа от оператора.
----------
15 + 5 в результате будет 20
20 + -3 в результате будет 17
13.4 + 7 в результате будет 20.4
----------
(-) Вычетание-Вычитает правый операнд из левого
----------
15 - 5 в результате будет 10
20 - -3 в результате будет 23
13.4 -7 в результате будет 6.4
----------
(*) Умножение-Перемножает операнды
----------
5 * 5 в результате будет 25
7 * 3.2 в результате будет 22.4
-3 * 12 в результате будет -36
----------
(/) Деление-Делит левый операнд на правый
----------
15 / 5 в результате будет 3
5 / 2 в результате будет 2 (В Python 2.x версии 
при делении двух целых чисел, результат будет 
целое число)
5.0 / 2 в результате будет 2.5 (Что бы получить
"Правильный" результат, хотя бы один операнд
должен быть float)
-----------
(%) Деление по модулю-Делит левый операнд на 
правый и возвращает остаток.
-----------
6 % 2 в результате будет 0
7 % 2 в результате будет 1
13.2 % 5 в результате будет 3.2
----------
(**) Возведение в степень-Возводит левый операнд 
в степень правого
----------
5 ** 2 в результате будет 25
2 ** 3 в результате будет 8
-3 ** 2 в результате будет -9
----------
(//) Целочисленное деление-Деление в котором 
возвращается только целая часть результата.
Часть после запятой, отбрасывается.
----------
12 // 5 в результате будет 2
4 // 3 в результате будет 1
25 // 6 в результате будет 4
'''


print(2 + -3)  # -1
print(2 - -7)  # 9
print(-14 * 2)  # -28
print(32 / 4)  # 8.0
print(5 / 2)  # 2.5
print(12 % 4)  # 0
print(7.2 % 2)  # должно быть 1.2
# но из за погрешности связанной со способом хранения числа
# будет 1.2000000000000002
print(0.1 + 0.2)  # погрешность 0.30000000000000004
print(3 ** 2)  # 9
print(5 ** 2)  # 25
print(11 // 2)  # 5
print(4 // 3)  # 1
"""

# Lesson #6 (Variable's)
"""
xInt = 1
yStr = 'a'
zFloat = 5.0

# функция type() показывает тип данных в переменной
print(type(xInt), type(yStr), type(zFloat))

# Переменные чувствительны к регистру
x = 0
X = 1
print(x, X)

# Указание переменных в одной строке
x = 0.1; y = 0.2  # Не рекомендуется

# Множественное присваивание значений переменным
x, y, z = (1, 2, 3)
print(y, x, z)

# Констант в Python нет, согласно соглашению*
# константы принято именовать полностью ЗАГЛАВНЫМИ
# если "повезёт" не переназначат =))
TEST_CONST = 'constanta'
print(TEST_CONST, type(TEST_CONST))

# Для неопределенных в момент обьявления переменных можно использовать значение None
newVariable = None
print(newVariable, type(newVariable))
newVariable = 'some type'
print(newVariable, type(newVariable))
"""

# Lesson #7 (Boolean data type)
"""
varBoolTrue = True
varBoolFalse = False

# int();str();float();bool();  # приведение к указанному типу данных

a, b, c, d = (1, 0, -1, None)
print('a ->', type(a), 'b ->', type(b), 'c ->', type(c), 'd ->', type(d))
print(int(a), str(b), float(c), bool(d))
a, b, c, d = (int(a), str(b), float(c), bool(d))
print('a ->', type(a), 'b ->', type(b), 'c ->', type(c), 'd ->', type(d))
"""

# Lesson #8 (String's)
"""
# \n перенос строки, \ экранирование символа, продление строки
oldWords = 'Hello, "test", \'test2\', World!'
print(oldWords)

# '''Многострочная строка 1''', \"""Многострочная строка 2\"""
words = ('Гордость и предубеждение Джейн Остин\n\
Учебник психологии отношений\n\
Два капитана Вениамин Каверин\n\
Учебник личностного роста')
print(words)
"""

# Lesson #9 (Operations with Strings)
"""
sWay = 'D:\\n\Python\\test.py'  # используем экранирование
sWay1 = '\n' + r'D:\n\Python\test.py'  # r означает что строка "сырая (все операторы в ней игнорируется)"
print(sWay, sWay1)

sPython = 'Py' 'thon'  # Склеивание / конкатенация
print(sPython)

sHello = 'Hello, my name is '
sName = 'John. I have old '
sResult = sHello + sName
iAge = 20  # Для конкатенации str + int нужно int привести к типу str()
print(sResult + str(iAge))

# Операция умножения со строками...
print((sResult + '\n') * 5)

# Табличка для понимания индексации и срезов строк...
+---+---+---+---+---+---+---+---+---+---+---+---+
| H | e | l | l | o |   | w | o | r | l | d | ! |
+---+---+---+---+---+---+---+---+---+---+---+---+
0   1   2   3   4   5   6   7   8   9  10  11  12
-12 -11 -10 -9  -8  -7  -6  -5  -4  -3  -2 -1

# Индексация строк
sIndex = 'Hello world!'
print(sIndex[6])  # Обращение по индексу строки

# срезы: variable[X:Y:Z] X - начало среза; Y - окончание; Z - шаг среза;
print(sIndex[0:5] + sIndex[5:12])  # Вывод требуемых фрагментов строки
print(sIndex[-1::-1])  # Вывод строки наоборот
print(sIndex[::-2])  # Вывод каждого 2го символа строки в обратном порядке
"""

# Lesson #10 (String Method's, Function)
"""
'''
# https://docs.python.org/3/library/stdtypes.html#string-methods
# https://pythonworld.ru/tipy-dannyx-v-python/stroki-funkcii-i-metody-strok.html

#String function
len(str) - Длина строки
str.capitalize() - Переводит первый символ строки в верхний регистр, а все остальные в нижний
str.center(width, [fill]) - Возвращает отцентрованную строку, по краям которой стоит символ fill (пробел по умолчанию)
str.count(str, [start],[end]) - Возвращает количество непересекающихся вхождений подстроки в диапазоне [начало, конец] 
(0 и длина строки по умолчанию)
str.find(str, [start],[end]) - Поиск подстроки в строке. Возвращает номер первого вхождения или -1
str.index(str, [start],[end]) - Поиск подстроки в строке. Возвращает номер первого вхождения или вызывает ValueError
str.replace(шаблон, замена) - Замена шаблона
str.split([символ])- Разбиение строки по разделителю

# Return boolean type
str.isdigit() - Состоит ли строка из цифр
str.isalpha() - Состоит ли строка из букв
str.isalnum() - Состоит ли строка из цифр или букв
str.islower() - Состоит ли строка из символов в нижнем регистре
str.isupper() - Состоит ли строка из символов в верхнем регистре
'''
s = 'hello,l Wo rld!'

# print('String Length = ' + str(len(s)))  # String Length = 13
# print(str.capitalize(s))  # Hello, world! первая буква заглавная а все остальные строчные
# print(s[-1::-1].center(22, '-'))  # ----!dlroW l,olleh---- вывод строки наоборот
# print('В строке', s[12:13].count('l', 0, 6), 'символа l')  # l функция не найдет из за ограничения среза s[12:13]
# print(s[::-1].find('W'))  # Поиск по индексу с конца строки к началу =)
# print(s[-5::-1].index('o', 1, 13)) Первое вхождение подстроки 'o' в строке s или исключение*

#sSelf = None
# int(); float(); str(); bool();
# print(s.replace('l', 'R',))
#d = (s[::-1].replace('l', str(sSelf), -1));  print(d)

# a = (s.find(s[::].replace(d, sSelf)))
# a = (s.find('l', s[::].replace(d, sSelf))) # не работает, разобраться позже
# print(a, '\n', d)
# print(s.split(' '))

s1 = '3hello,l Wo 2 rld!1'
# print(s1[-7:-8:-1].isdigit())  # указал срезом строки на цифру в строке
# print(s1[1:6:].isalpha())  # указал срезом на подстроку в строке состоящую из букв
# print('1) ', s1[:-2:-1].isalnum(), '\n2) ', s1[-3:-5:-1].isalnum())  # указал срезами на подстроки(цифры и символы)
# print(s1[:9:1].islower())  # указал срезом на подстроку в строке состоящую из строчных букв
# print('1)', s1[9:10:1].isupper())  # срез из подстроки состоит из букв верхнего регистра
"""

# Lesson #11 (String Formatting)
"""
name = 'Max'
age = 27
# # old format
# print('My name is ' + name + '. I\'m ' + str(age))
# print('My name is %(name)s. I\'m %(age)d' % {'name': name, 'age': age})  # Указываем маркером на переменную
# print('My name is %s. I\'m %d' %('MName', age))  # позиционные маркеры
# print('Title: %s. Pr %s ice: %.2f' % ('Google', name, 170))

# old-new, function ''.format()
# print('My {1} name is {0}. I\'m a {1} is old.'.format('Max', 27))  # Позиционные маркеры, функция .format()
# print('My name {a}. I\'m {b} is old'.format(a=name, b=age))
# print('My age is {}'.format(7 + 20))


# New python v_3.6 f-string
# print(f'My name is {name}. I\'m {age} is old =(')
# mName = 'M_12_NA_@$_ME'
# mAge = 27
# print(f'1) {mName[::].replace(str(12), str(mAge))}. \n2) {mAge*mAge}')
"""

# Lesson #12 (operator if)

# a = None
# b = 20
# if a:
#     print(True)
# else:
#     print(False)

# a = '2016996102'
# b = None
# if (int(a[-1:-5:-1]) - 16) == 2000:
#     b = 2000
#     print(f"Right!\na = {a, a[-1:-5:-1]} \nb = {b}")
# else:
#     print('Wrong')

# uAgeEtalon = 18
# uAge = int(input('Enter you age: '))
#
# if uAge >= uAgeEtalon:
#     print('Welcome')
# elif uAge < uAgeEtalon:
#     print(f'You can coming after {uAgeEtalon - uAge} years')
# else:
#     print('Stop')

# Logical operators: and, or, not
# a = int(input('Enter a = '.isdigit()))
# b = int(input('Enter b = '))

# print(if a = int(input('Enter a = '.isdigit()))  #Not work...
# print(a)

a = None
a = 123
b = 123
c = '321_Hello_123'
d = 3.14

if a != b:
    print('a != b')
else:
    print('a = b')

# commit









