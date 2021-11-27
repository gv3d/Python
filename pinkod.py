# функція генерує пінкод з цифр від 0 до 9 довжиною value і зберігає список у файл my_pinkod.txt
# замінє всі 5 на 6
import random
from typing import List

# функція генерує пінкод з чисел від 0 до 8 заданою довжиною length
def generate_pin(length: int) -> str:  # аннотація: ..int) -> str -  функція бере число, повертає рядок
    return ''.join(str(random.randint(0, 9)) for _ in range(length))


# функція замінює у списку a_list всі 5 на задане число value
def replace_fives(a_list: list, value: str) -> List[str]:
    return [element.replace('5', value) for element in a_list]

# функція записує результат в текстовий файл
def write_file(filename: str, data: str):
    with open(filename, 'w') as file:
        file.write(data)


if __name__ == '__main__':
    pins = [generate_pin(8) for _ in range(5)]  # генеруємо 8 пінкодів довжиною 5 цифр
    pins_without_fifes = replace_fives(pins, '6')  # замінюємо 5 на 6
    str_list = '\n'.join(pins_without_fifes)  # виводимо пінкоди в стовбчик
    print(pins_without_fifes)
    write_file('my_file_with_pinkod.txt', str_list)  # записуємо результат у файл my_file_with_pinkod.txt
