def solution(a):
  n = max(a) + 1
  counts = [0] * n

  for el in a:
    if(el > 0):
      counts[el] += 1

  if(len(counts) == 0):
    return 1
    
  for idx, el in enumerate(counts[1:]):
    if(el == 0):
      return idx + 1
  
  return n
  


def test_solution():
  assert solution([1,3,6,4,1,2]) == 5
  assert solution([1,2,3]) == 4
  assert solution([-1, -3]) == 1