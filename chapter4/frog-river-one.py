def solution(x, a):
  total = x * (x + 1) // 2
  counted = {}
  for idx, el in enumerate(a):
    if(not counted.get(el)):
      counted[el] = True
      total = total - el

    if(total == 0):
      return idx

  return -1

def test_solution():
  assert solution(5, [1,3,1,4,2,3,5,4]) == 6
  assert solution(1, [1]) == 0
  assert solution(5, [3]) == -1