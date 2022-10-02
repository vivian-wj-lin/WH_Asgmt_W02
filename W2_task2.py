# 要求二:Python字典與列表、JavaScript物件與陣列

def avg(data):

    # 1.拿字典 的 key 'employees' 的 value
    # 2.用for迴圈加判斷式:如果key 'manager'值是false,則抓取key 'salary'的資料
    # 3.計算抓取出的salary value平均值

    employees = data['employees']

    total = 0
    amount = 0

    for e in employees:
        # print(e)

        # 檢查是不是 manager
        if e['manager'] == True:
            continue
        # print(e)

        total += e['salary']
        amount += 1

    # print(totoal)
    # print(amount)
    answer = total / amount
    print(answer)

    return answer


avg({
    "employees": [
        {
            "name": "John", "salary": 30000, "manager": False
        },
        {
            "name": "Bob", "salary": 60000, "manager": True
        },
        {
            "name": "Jenny", "salary": 50000, "manager": False
        },
        {
            "name": "Tony", "salary": 40000, "manager": False
        }
    ]
})  # 呼叫 avg 函式
