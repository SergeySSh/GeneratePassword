"""Программа генерирует пароли любой сложности и длины, соответствующей заданным условиям."""
from random import choice

numbers = [i for i in range(48, 65)]  # цифры
simbols = [i for i in range(33, 49)]  # символы
letters = [i for i in range(65, 91)]  # буквы верхнего регистра
letters_lower = [i for i in range(97, 123)]  # буквы нижнего регистра
letters_rus = [i for i in range(1040, 1073)]  # русские буквы верхнего регистра
letters_rus_lower = [i for i in range(1072, 1105)]  # русские буквы нижнего регистра


def generate_password(length: int, complexity: str):
    """Генерирует пароль."""
    if complexity == 'simple':
        complexity_symbols = numbers + simbols
    elif complexity == 'easy':
        complexity_symbols = numbers + simbols + letters_lower
    elif complexity == 'normal':
        complexity_symbols = numbers + simbols + letters + letters_lower
    elif complexity == 'hard':
        complexity_symbols = numbers + simbols + letters + letters_lower + letters_rus + letters_rus_lower
    else:
        raise ValueError('Invalid complexity level. Choose from simple, easy, normal, hard.')

    password = []
    for _ in range(length):
        password.append(choice(complexity_symbols))

    return ''.join(chr(i) for i in password)


def main():
    length = int(input('Enter password length: '))
    complexity = input('Enter complexity level (simple, easy, normal, hard): ').lower()
    print('Generated password:', generate_password(length, complexity))


if __name__ == '__main__':
    main()
