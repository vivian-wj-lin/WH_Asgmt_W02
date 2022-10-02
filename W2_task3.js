
// 要求三: 找出至少包含兩筆整數的列表 (Python) 或陣列 (JavaScript) 中,兩兩數字相乘後的最大值。
// function中的function 

function func(a) {
  function f(b, c) {
    answer = a + b * c
    console.log(answer)
    return answer
  }

  return f
}

func(2)(3, 4); // 你補完的函式能印出 2+(3*4) 的結果 14
func(5)(1, -5); // 你補完的函式能印出 5+(1*-5) 的結果 0
func(-3)(2, 9); // 你補完的函式能印出 -3+(2*9) 的結果 15
            // 一般形式為 func(a)(b, c) 要印出 a+(b*c) 的結果


