"""
Задача №4
Користувач вводить рядок,
в якому можуть бути присутні пропуски.
Визначити, чи є рядок паліндромом,
тобто таким, який однаково читається як справа наліво,
так і зліва направо. Для літер регістр не враховувати.
Приклади рядків-паліндромів: racecar, 10201, Ada, Never odd or even
"""

row = input('рядок: ').lower()
origin_list = [i for i in [*row] if i != ' ']
new_list = list(reversed([i for i in [*row] if i != ' ']))
counter = 0

for index, char in enumerate(origin_list):
    if char == new_list[index]:
        counter += 1

print('паліндром') if counter == len(origin_list) else print('не паліндром')
