"""
Напишите функцию update_dictionary(d, key, value), которая принимает на вход словарь d и два числа: key и value.

Если ключ key есть в словаре d, то добавьте значение value в список, который хранится по этому ключу. 
Если ключа key нет в словаре, то нужно добавить значение в список по ключу 2⋅key. Если и ключа 2⋅key нет, то нужно добавить ключ 2⋅key в словарь и сопоставить ему список из переданного элемента [value].

Требуется реализовать только эту функцию, кода вне неё не должно быть.
Функция не должна вызывать внутри себя функции input и print.

Пример работы функции:

d = {}
print(update_dictionary(d, 1, -1))  # None
print(d)                            # {2: [-1]}
update_dictionary(d, 2, -2)
print(d)                            # {2: [-1, -2]}
update_dictionary(d, 1, -3)
print(d)                            # {2: [-1, -2, -3]}
﻿"""
def update_dictionary(d, key, value):
	if d.get(key) != None:
		d[key].append(value)
		
	elif d.get(2*key) != None:
		d[2*key].append(value)

	else:
		d[2*key] = [value]


k = {}
update_dictionary(k,1,200)


update_dictionary(k,2,200)
update_dictionary(k,2,300)
update_dictionary(k,2,500)
update_dictionary(k,1,500)

print(k)


"""
def update_dictionary(d, key, value):
    (d.setdefault(key * (2 - (key in d)), [])).append(value)

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
(\\\\1////)
def update_dictionary(d, key, value):
    key += key * (key not in d)
    d[key] = d.get(key, []) + [value]




True -> 1

False -> 0

key += key * (key not in d)
приплюсовывает к значению key его же, в случае когда key not in d, в ином случае приплюсовывается 0.
Таким образом, если ключа нет в словаре то выражение вычисляется как:
key += key * 1
Когда ключ уже есть:
key += key * 0
key += 0 # к значению добавляется 0, т.е. оно не изменяется
Это происходит из-за того что результат вычисления выражения key not in d может быть только True или False, которые затем при попытке умножения конвертируются True -> 1, False -> 0.
Далее значение просто добавляется в список.

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

def update_dictionary(d, key, value):
    if key in d:
        d[key].append(value)
    else:
        if 2*key not in d : d[2*key] = []
        update_dictionary(d, 2*key, value)

use function recursive

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

example_1: смотреть на первый пример (\\\\1////)

def update_dictionary(d, key, value): 
    d.setdefault(key+key*(key not in d),[]).append(value)


example_2:

def update_dictionary(d, k, v):
    if k in d:
        d.setdefault(k, []).append(v)
    else:
        d.setdefault(k*2, []).append(v)
 \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

def update_dictionary(d, key, value):
    key <<= key not in d
    d.setdefault(key,[]).append(value)


 Как я понял, здесь смещается влево на 0 (true), если ключ существует и на 1 (false) если ключа нет
Смещение влево на 1 равносильно умножению на 2 (если не случается overflow)

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

>>>>>  использование try ... execpt <<<<<<<<<<<

example_1:

def update_dictionary(d, key, value):
    try:
        d[key].append(value)
    except KeyError:
        d.setdefault(2*key, []).append(value)

example_2:

def update_dictionary(d, key, value):
        try:
            d[key].append(value)
        except:
            try:
                d[2*key].append(value)
            except:
                d[2*key] = [value]

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
"""