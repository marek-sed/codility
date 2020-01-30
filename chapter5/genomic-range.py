from itertools import accumulate

impact = {
  "A": 1, "C": 2, "G": 3, "T":4
}
def letterImpact(l, s):
  i = impact[l]
  imps = [0] + [impact[x] for x in s]
  
  return list(accumulate(imps, lambda x, y: x + 1 if y == i else x))

def solution(s, p, q):
  apacts = letterImpact("A", s) 
  cpacts = letterImpact("C", s) 
  gpacts = letterImpact("G", s) 
  tpacts = letterImpact("T", s) 

  result = []
  for (start, end) in zip(p, q):
    if apacts[end + 1] - apacts[start] > 0:
      result.append(1)
    elif cpacts[end + 1] - cpacts[start] > 0:
      result.append(2)
    elif gpacts[end + 1] - gpacts[start] > 0:
      result.append(3)
    elif tpacts[end + 1] - tpacts[start] > 0:
      result.append(4)
    
  return result

def test_letterImpact():
  assert letterImpact("A", "CAGCCTA") == [0, 0, 1, 1, 1, 1, 1, 2]

def test_solution():
  assert solution("CAGCCTA", [2,5,0], [4,5,6]) == [2,4,1]
  assert solution("A", [0], [0]) == [1]
