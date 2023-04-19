def count_change(total):
    # Список номиналов монет
    denominations = [1, 5, 10, 25]
    
    # Рекурсивная функция для подсчета количества вариантов размена
    def cc(amount, coins_available):
        # Базовый случай
        if amount == 0:
            return 1
        # Если сумма отрицательная или закончились монеты, возвращаем 0
        if amount < 0 or not coins_available:
            return 0
        # Рекурсивный случай
        else:
            # Количество вариантов размена без использования текущей монеты
            ways_without_coin = cc(amount, coins_available[:-1])
            # Количество вариантов размена с использованием текущей монеты
            ways_with_coin = cc(amount - coins_available[-1], coins_available)
            # Возвращаем сумму обоих случаев
            return ways_without_coin + ways_with_coin
    
    # Вызываем рекурсивную функцию для подсчета количества вариантов размена
    return cc(total, denominations)
