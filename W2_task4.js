
//  要求四: 函式與流程控制

function maxProduct(nums) {
  let answer = -Infinity
  for (let i = 0; i < nums.length - 1; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      const x = nums[i] * nums[j]
      if (x > answer) {
        answer = x
      }
    }
  }
  console.log(answer)
  return answer
}

maxProduct([5, 20, 2, 6]) // 得到 120
maxProduct([10, -20, 0, 3]) // 得到 30
maxProduct([10, -20, 0, -3]) // 得到 60
maxProduct([-1, 2]) // 得到 -2
maxProduct([-1, 0, 2]) // 得到 0 或 -0
maxProduct([5, -1, -2, 0]) // 得到 2
maxProduct([-5, -2]) // 得到 10
