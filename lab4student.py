#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000 #стипендия, расходы за проживание

# TODO здесь ваш код
expenses_in_month, expenses_all = expenses, expenses
i = 1
while i < 10:
    expenses_in_month = expenses_in_month * 1.03
    expenses_all = expenses_all + expenses_in_month
    i += 1
result = expenses_all - educational_grant * 10
print('Студенту надо попросить', result, 'рублей.')
