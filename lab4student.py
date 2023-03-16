educational_grant, expenses = 10000, 12000
i = 0
month_expenses = 0
money = 0
need = educational_grant
while i < 10: 
    if i == 0:
        month_expenses = expenses
    elif i >= 1: 
        month_expenses *= 1.03
    i += i
    diference = round(month_expenses-need, 2)
    money += diference 
print('Studentu nado poprosit', money, 'rub')
