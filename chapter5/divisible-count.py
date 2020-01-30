def solution(a, b, k):
  s = 0
  if (a % k == 0):
    s = a // k -1
  else:
    s = a // k
  
  e = b // k

  return e - s

def test_solution():
  assert solution(7, 11, 2) == 2
  assert solution(6, 11, 2) == 3
  assert solution(6, 12, 2) == 4
  assert solution(6, 12, 3) == 3
  assert solution(1, 1, 11) == 0
  assert solution(0, 1, 11) == 0
  assert solution(0, 0, 11) == 1
  assert solution(11, 345, 17) == 20
