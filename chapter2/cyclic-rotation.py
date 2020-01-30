def solution(a, k):
  if (a == []): return a
  while k > 0:
    k = k - 1
    a = [a.pop()] + a

  return a

def test_solution():
  assert solution([], 5) == []
  assert solution([1, 2, 3 ,4], 2) == [3, 4, 1, 2]