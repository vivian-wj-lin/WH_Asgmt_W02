
// 要求五:在一組陣列中找出兩個數，其加總恰等於給定值。每個數不能被重複使用，且必剛好只有一個解。
// 就是要求四的進階題!

function twoSum(nums, target) {
  for (let i = 0; i < nums.length - 1; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      let x = nums[i] + nums[j]
      if (x === target) {
        return [i, j]
      }
    }
  }
}

let result = twoSum([2, 11, 7, 15], 9);
console.log(result); // show [0, 2] because nums[0]+nums[2] is 9

