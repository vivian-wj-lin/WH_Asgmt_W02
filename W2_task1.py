# 要求一: 函式與流程控制

# 創建calculate函式中的list
# 創建函式、賦值(NewList的總和函式)
# 印出NewList所有數字加總

def calculate(min, max, step):
    NewList = range(min, max+1, step)
    # print(list(NewList))
    NewListSum = sum(NewList)
    print(NewListSum)


calculate(1, 3, 1)
calculate(4, 8, 2)
calculate(-1, 2, 2)
