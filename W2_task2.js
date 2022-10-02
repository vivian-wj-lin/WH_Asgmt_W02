
//  要求二:Python字典與列表、JavaScript物件與陣列

function avg(data) {

  const employees = data.employees

  let total = 0
  let amount = 0

  for (let e of employees) {
    // console.log(e)
    if (e['manager'] === true) {
      continue
    }
    total += e['salary']
    amount += 1
  }

  const answer = total / amount
  console.log(answer)
  return answer

}


avg({
  "employees": [
    {
      "name": "John", "salary": 30000, "manager": false
    },
    {
      "name": "Bob", "salary": 60000, "manager": true
    },
    {
      "name": "Jenny", "salary": 50000, "manager": false
    },
    {
      "name": "Tony", "salary": 40000, "manager": false
    }
  ]
}); // 呼叫 avg 函式


