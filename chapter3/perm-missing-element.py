def solution(a):
  if len(a) == 0: 
    return 1
  
  n = max(a)
  
  result = (n * (n + 1) // 2) - sum(a)
  if (result == 0):
    return n + 1
  
  return result

def test_solution():
  assert solution([2,3,1,5]) == 4
  assert solution([]) == 1
  assert solution([2,3,4,5]) == 1
  assert solution([1, 2, 3,4, 5]) == 6
  assert solution([1]) == 2
  assert solution([1, 2]) == 3