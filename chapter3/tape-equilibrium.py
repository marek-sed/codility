from itertools import accumulate, islice
from operator import add

def solution(a):
  psums_lr = list(accumulate(a, add))
  psums_rl = list(islice(reversed(list(accumulate(reversed(a), add))), 1, None))

  diffs = [abs(x - y) for (x, y) in zip(psums_lr, psums_rl)]

  return min(diffs)

def test_solution():
  assert solution([3, 1, 2, 4, 3]) == 1
  assert solution([1, 1]) == 0