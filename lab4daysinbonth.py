user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input)
month_dict = {1: '31', 2: '28', 3: '31', 4: '30', 5: '31', 6: '30', 7: '31', 8: '31', 9: '30', 10: '31', 11: '30', 12: '31',}
if month in month_dict: 
    print('Days in a month:', month_dict[month])
else:
    print('None')    