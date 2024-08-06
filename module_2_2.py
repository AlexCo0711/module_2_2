first = int(input("Введите первое целое число: "))  # ввод исходных данных1
second = int(input("Введите второе целое число: "))  # ввод исходных данных2
third = int(input("Введите третье целое число: "))  # ввод исходных данных3
# вариант 1
if first == second == third:  # условие равенства всех введенных чисел (если)
    print('3')
elif first == second != third or second == third != first or first == third != second:  # условие равенства 2-х из 3-х введенных чисел (если, то)
    print('2')
else:  # условие, когда не выполняются первые два условия (иначе)
    print('0')
# вариант 2
if first == second and second == third:  # условие равенства всех введенных чисел (если)
    print('3')
elif first == second and first != third or second == third and second != first or first == third and first != second:  # условие равенства 2-х из 3-х введенных чисел (если, то)
    print('2')
else:  # условие, когда не выполняются первые два условия (иначе)
    print('0')
# вариант 1 предпочтительней, вероятность внесения ошибки меньше.