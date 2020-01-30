def solution(a):
  col = []

  for idx, el in enumerate(a):
    col.append((idx - el, idx + el))
  
  col.sort(key=lambda x: x[0])
  ends = sorted(col, key=lambda x: x[1])
  print(col)
  print(ends)
  counts = 0
  for idx, (s, e)  in enumerate(col):
    print(list(i for i, (x, y) in enumerate(col[(idx + 1):]) if e > x))
    print(idx, eidx)
    counts += eidx - idx
  
  return counts

def test_solution():
  assert solution([1, 5, 2, 1, 4, 0]) == 11