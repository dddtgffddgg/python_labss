def falling(n, k):
    """Рассчитать убывающий факториал от n глубины k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    if k == 0:
        return 1
    return n*falling(n-1, k-1)


def sum_digits(y):
    """Сложить все цифры числа y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123)
    >>> a
    6
    """
    number = int(input("Введите число: "))
    sum = 0
    while number > 0:
        digit = number % 10
        sum += digit
        number //= 10
    print("Сумма цифр введенного числа: ", sum)



def double_eights(n):
    """Возвращает True если в n есть две цифры 8 подряд.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    n = int(input("Введите число: "))
    s = str(n)
    
    if "88" in s:
        print("Число содержит две цифры 8 подряд.")
    else:
        print("В числе нет двух цифр 8 подряд.")
    
