def solution(n, a):
  result = [0] * n

  max = 0
  resetValue = 0
  for i in a:
    if i == n + 1:
      resetValue = max
      continue
    elif result[i -1] < resetValue:
      result[i - 1] = resetValue + 1
    else:
      result[i - 1] += 1
    
    if result[i - 1] > max:
      max = result[i - 1]

  return list(map(lambda x: x if x > resetValue else resetValue, result))

def test_solution():
  assert solution(5, [3, 4, 4, 6, 1, 4, 4]) == [3, 2, 2, 4, 2]
  