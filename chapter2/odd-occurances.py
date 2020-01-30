def solution(a):
  sum = 0
  for i in a:
    sum ^= i
  
  return sum

def test_solution():
  assert solution([9, 3, 9, 3, 9, 7, 9]) == 7
  assert solution([9, 3, 9, 3, 9, 7, 9, 7, 7]) == 7