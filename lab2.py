mod = 10  #Способ 1
for i in range(1, 1001): 
    if i == mod:
        mod *= 10 
    if (i*i) % mod == i:
        print(i)

for i in range(1, 1001):  #Способ 2
    res = len(str(i))
    if i == (i**2) % 10 ** res:
        print(i)   
