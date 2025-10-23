envelop_x, envelop_y = 10, 5
paper_x = int(input()) #paper_y = 8, 9
paper_y = int(input())
# проверить для
#paper_x, paper_y = 9, 8
#paper_x, paper_y = 6, 8
#paper_x, paper_y = 8, 6
#paper_x, paper_y = 3, 4
#paper_x, paper_y = 11, 9
#paper_x, paper_y = 9, 11
# (просто раскоментировать нужную строку и проверить свой код)

if paper_x > envelop_x or paper_y > envelop_y:
    if paper_y > envelop_x or paper_x > envelop_y:
        print('No')
    else: 
        print('Yes')
else: 
    print("Yes")    
