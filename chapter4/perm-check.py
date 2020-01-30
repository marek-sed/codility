def solution(a):
  m = max(a)
  total = m * (m + 1) // 2
  counted = {}
  for el in a:
    c = counted.get(el)
    if not c:
      counted[el] = 1
      total -= el
    else:
      return 0
    
    
  if total == 0:
    return 1
  else: 
    return 0

def test_solution():
  assert solution([4,1,3,2]) == 1
  assert solution([4,1,3]) == 0 
  assert solution([1, 1]) == 0
  assert solution([9, 5, 7, 3, 2, 7, 3, 1, 10, 8]) == 0