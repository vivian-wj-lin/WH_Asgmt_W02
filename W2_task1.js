//  要求一: 函式與流程控制

function calculate(min, max, step) {
  let total = 0
  for (let i = min; i <= max; i += step) {
    // console.log(i);
    total += i;
  }
  console.log(total);
}

calculate(1, 3, 1);
calculate(4, 8, 2);
calculate(-1, 2, 2);
