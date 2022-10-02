#要求四: 函式與流程控制

def maxProduct(nums):
    # [5, 20, 2, 6]
    # 5 * 20
    # 5 * 2
    # 5 * 6

    # 20 * 2
    # 20 * 6

    # 2 * 6

    # 印出
    # 5, 20
    # 20, 2
    # 2, 6

    answer = float('-inf')  # 最小值

    for i in range(len(nums) - 1):  # 5,20,2
        # print(i, nums[i])
        # print(nums[i], nums[i + 1])

        # print(i)
        for j in range(i + 1, len(nums)):  # 從 i 的下一個開始, 跑完 nums
            # print(i, j)  # 0,1 0,2, 0,3, 1,2, 1,3, 2,3
            # print(nums[i], nums[j])

            x = nums[i] * nums[j]
            # print(x)

            if x > answer:
                answer = x

    print(answer)
    return answer


maxProduct([5, 20, 2, 6])  # 得到 120
maxProduct([10, -20, 0, 3])  # 得到 30
maxProduct([10, -20, 0, -3])  # 得到 60
maxProduct([-1, 2])  # 得到 -2
maxProduct([-1, 0, 2])  # 得到 0
maxProduct([5, -1, -2, 0])  # 得到 2
maxProduct([-5, -2])  # 得到 10
