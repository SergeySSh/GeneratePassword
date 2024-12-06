"""Программа генерирует пароли любой сложности и длины, соответствующей заданным условиям."""
from random import randint, choice

numbers = [48, 58]  # цифры
simbols = [33, 48]  # символы
letters = [65, 90]  # буквы верхнего регистра
letters_lower = [97, 122]  # буквы нижнего регистра
letters_rus = [1040, 1072]  # русские буквы
letters_rus_lower = [1072, 1104]  # русские буквы нижнего регистра


def generate_password(length: int, complexity: str):
    """Генерирует пароль."""
    if complexity == 'easy':
        complexity_symbols = numbers + simbols + letters_lower
    elif complexity == 'normal':
        complexity_symbols = numbers + simbols + letters + letters_lower
    elif complexity == 'hard':
        complexity_symbols = numbers + simbols + letters + letters_lower + letters_rus + letters_rus_lower
    else:
        raise ValueError('Invalid complexity level. Choose from easy, normal, hard.')

    password = []
    for _ in range(length):
        password.append(choice(complexity_symbols))

    return ''.join(chr(i) for i in password)


def main():
    length = int(input('Enter password length: '))
    complexity = input('Enter complexity level (easy, normal, hard): ').lower()
    print('Generated password:', generate_password(length, complexity))


if __name__ == '__main__':
    main()
