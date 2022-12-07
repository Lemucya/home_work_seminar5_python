"""
3) Создать текстовый файл (не программно), построчно записать фамилии
сотрудников и величину их окладов (не менее 10 строк). Определить, кто из
сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
"""

report = []
sum_salaries = 0
with open('file_task_03.txt', 'r', encoding='UTF-8') as file:
    rows = file.readlines()
    print("Оклады сотрудников")
    for row in rows:
        row_items = row.split(' ')
        report.append([row_items[0], int(row_items[1])])
        print(f"{row_items[0]}: {int(row_items[1])} руб.")
        sum_salaries += int(row_items[1])

print("\nСотрудники с окладом менее 20000 руб.")
[print(worker[0]) for worker in report if worker[1] < 20000]

print(f"\nСредний оклад сотрудников {sum_salaries / len(report)} руб.")
