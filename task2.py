"""
Задача №2
Дано п’ятизначне десяткове число.
Побудуйте нове десяткове число за наступними правилами.
Необхідно обчислити два числа, з яких перше - це сума першої, третьої та п’ятої цифр
і друге число - це сума другої і четвертої цифр введеного числа.
Відповідь - це отримані два числа, які записуються один за одним в одному рядку.
Автор: Задворна Анастасія Богданівна
"""

number = input('Число: ')
first, second, third, firth, fifth = number
print(f'{int(first) + int(third) + int(fifth)}{int(second) + int(firth)}')
