def solution(a):
  found = {}
  count = 0
  for el in a:
    if(not found.get(el)):
      found[el] = True
      count += 1

  return count

def test_solution():
  solution([2, 1, 2, 1, 1, 3]) == 3