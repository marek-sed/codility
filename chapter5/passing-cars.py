from itertools import accumulate
from operator import add

def solution(a):
  psums = list(accumulate(a, add))
  count = 0
  for idx, el in enumerate(a):
    if el == 0:
      count += psums[-1] - psums[idx]

  return count if count <= 1000000000 else -1

def test_solution():
  assert solution([0, 1, 0, 1, 1]) == 5