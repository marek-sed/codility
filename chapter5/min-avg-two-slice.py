from itertools import combinations

def solution(a):
  pos = 0
  min_avg = (a[0] + a[1]) / 2
  for i in range(2, len(a)):
    avg2 = (a[i-1] + a[i]) / 2
    avg3 = (a[i-2] + a[i-1] + a[i]) / 3

    if (avg3 < min_avg):
      min_avg = avg3
      pos = i-2
    
    if avg2 < min_avg:
      min_avg = avg2
      pos = i-1

  return pos


def test_solution():
  assert solution([4, 2, 2, 5, 1, 5, 8]) == 1
  assert solution([4, 3, 1, 1]) == 2
  assert solution([-2, 2, -5]) == 0
  assert solution([1, 10, 1]) == 0