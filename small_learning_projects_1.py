# УГАДАЙКА ЧИСЕЛ
# Описание проекта: программа генерирует случайное число в диапазоне от 1 до 100 и просит
# пользователя угадать это число.
# Если догадка пользователя больше случайного числа, то программа должна вывести сообщение
# 'Слишком много, попробуйте еще раз'. Если догадка меньше случайного числа, то программа должна вывести сообщение
# 'Слишком мало, попробуйте еще раз'. Если пользователь угадывает число, то программа должна поздравить его и
# вывести сообщение 'Вы угадали, поздравляем!'.
print(2**5+2**4+2**3+2**2+2+1)

from random import randint
print('Добро пожаловать в числовую угадайку!')#, 'n_rand =', n_rand)
print('АІ должен выбрать число от 1 до N, которое вам предстоит угадать.')

def is_valid(n):
    return n.isdigit() and 1 <= int(n) <= int(right)  # проверка числа на корректность

again = 'да'
while again == 'да':  # бесконечная игра пока "да"
    while True:
        right = input('\n' + 'Введите число N: ')  # указание правой границы диапазона
        if is_valid(right): # проверка числа на корректность
            right = int(right)
            print('OK')
            print()
            break
        else:
            print('Нужно ввести ЦЕЛОЕ ЧИСЛО')

    n_rand = randint(1, int(right))  # диапазон для угадывания
    c = 0  # счетчик попыток

    while True:  # безконечный цыкл попыток, пока не угадаешь
        n = input(f'Введите целое число от 1 до {right} включительно: ')
        if is_valid(n): # проверка числа на корректность
            c += 1
            n = int(n)
            if n < n_rand:
                print('Ваше число МЕНЬШЕ загаданного, попробуйте еще разок' + '\n')
                continue
            elif n > n_rand:
                print('Ваше число БОЛЬШЕ загаданного, попробуйте еще разок' + '\n')
                continue
            elif n == n_rand:
                if c % 10 == 1 and c % 100 != 11:
                    p = f'Вам понадобилась {c} попытка'
                elif n % 10 in [2, 3, 4] and n % 100 not in [12, 13, 14]:
                    p = f'Вам понадоболсь {c} попытки'
                else:
                    p = f'Вам понадобилось {c} попыток'
                print('ВЫ УГАДАЛИ, ПОЗДРАВЛЯЕМ!', '\n' + p)
                break
        else:
            print(f'А может быть все-таки введем целое число от 1 до {right}?' + '\n')
    again = input('\n' + 'Хотите сыграть еще разочек? (да/нет): ' + '\n')
    if again.lower() == 'нет':  # закончить цикл, если ввели "нет"
        break

print('Спасибо, что играли в числовую угадайку.')

