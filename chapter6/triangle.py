def solution(a):
  a.sort()

  for (x, y ,z) in zip(a, a[1:], a[2:]):
    print(x, y, z)
    if x + y > z and x + z > y and y + z > x:
      return 1
  
  return 0

def test_solution():
  assert solution([10, 5, 1, 20, 2, 8]) == 1
  assert solution([10, 5, 1, 50]) == 0
  assert solution([5, 3, 3]) == 1
