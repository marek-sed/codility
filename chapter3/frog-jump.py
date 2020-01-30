from math import ceil

def solution(x, y, d):
  return ceil((y - x) / d)

def test_solution():
  assert solution(10, 85, 30) == 3
  assert solution(10, 100, 10) == 9
  assert solution(10, 11, 10) == 1