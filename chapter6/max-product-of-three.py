def solution(a):
  a.sort()
  
  prod1 = a[-3] * a[-2] * a[-1]
  prod2 = a[0] * a[1] * a[-1]
  print(a)
  return max(prod1, prod2)

def test_solution():
  assert solution([-3, 1, 2, -2, 5, 6]) == 60
  assert solution([-3, -5, 2, -2, 5]) == 75
  assert solution([-10, -2, -4]) == -80