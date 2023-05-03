#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Составить список всех живущих на районе (пакет district) и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

from district.central_street.house1 import room_1 as r1h1cs, room_2 as r2h1cs
from district.central_street.house2 import room_1 as r1h2cs, room_2 as r2h2cs
from district.central_street.house1 import room_1 as r1h1cs, room_2 as r2h1cs
from district.central_street.house2 import room_1 as r1h2cs, room_2 as r2h2cs

rooms = [
    r1h1cs.folks, 
    r2h1cs.folks,
    r1h1cs.folks, 
    r2h1cs.folks,

]

roomfolks = []
for x in rooms:
    roomfolks.extend(x)
print("на районе живут: ", ','.join(roomfolks))    


