def solution(n):
  i = n
  count = 0
  isOpen = False
  gap = 0
  
  while i > 0:
    m = i % 2
    if m == 1 and isOpen:
      gap = max(count, gap)    
      count = 0
    elif m == 1 and not isOpen:
      isOpen = True
    elif m == 0 and isOpen:
      count = count + 1
      
    i = i // 2
  
  return gap

def test_solution():
  assert solution(1041) == 5
  assert solution(20) == 1
  assert solution(5) == 1
  assert solution(32) == 0