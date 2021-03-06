# Вывести два списка случайных 10 чисел от 1 до 50
# Проверить есть ли повторяющиеся числа в этих списках и вывести эти числа

# import random
# a = [random.randint(1,50) for i in range(10)]
# b = [random.randint(1,50) for i in range(10)]
# print(a)
# print(b)
# a = set(a)
# b = set(b)
# c = a & b
# print(*c)


# В кинотеатре есть кинозал, в котором находится
# 5 рядов по 10 мест в каждом ряде. Билеты на сеанс для детей до 3 лет бесплатные,
# с 3 до 12 лет и пенсионерам цена льготная, для всех остальных полная стоимость билета.
# Перед покупкой билета для пользователя вывести га экран все свободные места в кинозале.
# Пользователь выбирает ряд, место и покупает билет по цене, в зависимости от возрастной группы.
# Перед покупкой второго билета ввывести на экран оставшиеся свободные места.
# В конце напечатать полную стоимость всех купленных билетов.

print('-'*14, 'Свободные места', '-'*14)
cinema = {1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          2: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          3: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          4: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          5: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          }
for key, values in cinema.items():
    print('Ряд', key, '- места', values)
print('-'*45)
cost = []
c_1 = 0
c_2 = 5
c_3 = 10
while True:
    try:
        key = int(input('Выберите номер ряда: '))
        m = int(input('Выберите место: '))
        age = int(input('Ваш возраст: '))
        cinema[key].remove(m)
    except KeyError:
        print('Такой ряд или место отсутствует в кинозале!')
        continue
    except ValueError:
        print('Введены некорректные данные! Повторите запрос!')
        continue

    print('-' * 45)
    if age < 3:
        cost.append(c_1)
        print('Ваш билет: ряд', key, ', место', m, '\nСтоимость билета -', c_1, 'руб')
    elif age <= 12 or age >= 60:
        cost.append(c_2)
        print('Ваш билет: ряд', key, ', место', m, '\nСтоимость билета -', c_2, 'руб')
    else:
        cost.append(c_3)
        print('Ваш билет: ряд', key, ', место', m, '\nСтоимость билета -', c_3, 'руб')

    a = input('Желаете купить ещё один билет? Напишите да или нет: ')
    if a == 'да':
        print('-' * 14, 'Свободные места', '-' * 14)
        for key, values in cinema.items():
            print('Ряд', key, '- места', values)
        print('-' * 45)
    else:
        print('-' * 45)
        print('Общая стоимость: ', sum(cost), 'руб', '\nПриятного просмотра!')
        break

