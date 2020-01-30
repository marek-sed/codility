function solution(N) {
  // write your code in JavaScript (Node.js 8.9.4)
  const root = Math.floor(Math.sqrt(N))
  
  let minPerimeter = Number.MAX_SAFE_INTEGER;
  for (let i = 1; i <= root; i++) {
      if (N % i === 0) {
          const v = N / i
          minPerimeter = Math.min(minPerimeter, 2 * (v + i))
      }
  }
  
  return minPerimeter
}