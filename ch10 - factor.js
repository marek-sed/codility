function solution(N) {
  if (N === 1) return 1
  // n = 24 // 4
  // n = 16 // 1 2 4 8 16
  const root = Math.floor(Math.sqrt(N))
  
  let count = 0
  for (let i = 1; i <= root; i++) {
      if(N % i === 0) {
          if(root * i === N) count += 1
          else count += 2
      }
  }
  
  return count
}